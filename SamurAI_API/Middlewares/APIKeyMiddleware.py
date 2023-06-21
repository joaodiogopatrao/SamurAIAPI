from django.http import JsonResponse, HttpResponseForbidden
from django.conf import settings

from SamurAI_API.settings import VALID_API_KEYS


class APIKeyAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        if not self.verify_api_key(api_key):
            return HttpResponseForbidden('Invalid API key')

        token = self.generate_token(api_key)
        request.META['HTTP_AUTHORIZATION'] = f'Token {token}'

        return self.get_response(request)

    def verify_api_key(self, api_key):
        return api_key in settings.API_KEYS

    def generate_token(self, api_key):
        from rest_framework.authtoken.models import Token

        token, _ = Token.objects.get_or_create(key=api_key)
        return token.key

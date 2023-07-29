from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt

def is_authorized(request):
    token = request.COOKIES.get('jwt')

    if not token:
        token = request.headers.get('Authorization')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    return payload

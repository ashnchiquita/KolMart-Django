from rest_framework.views import APIView
from ..models import User
from django.conf import settings
from .utils import validate_email, createResponse
from rest_framework import status
import jwt, datetime

class LoginView(APIView):
    def post(self, request):
        try:
            username_email = request.data['username_email']
            password = request.data['password']

            if validate_email(username_email):
                user = User.objects.filter(email=username_email).first()
            else:
                user = User.objects.filter(username=username_email).first()

            if user is None:
                return createResponse(False, "User not found", None, status=status.HTTP_400_BAD_REQUEST)

            if not user.check_password(password):
                return createResponse(False, "Invalid credentials", None, status=status.HTTP_401_UNAUTHORIZED)

            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')

            response = createResponse(True, "Login succes", {
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'password': user.password
                },
                'token': token
            })

            response.set_cookie(key='jwt', value=token, httponly=True)

            return response
        except Exception as e:
            return createResponse(False, str(e), None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

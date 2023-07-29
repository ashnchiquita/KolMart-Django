from rest_framework.response import Response
from rest_framework import status
import re

def validate_email(email):
    return re.fullmatch(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)

def validate_username(username):
    return re.fullmatch(r'^[a-zA-Z0-9]+$', username)

def validate_password(password):
    return len(password) > 4

def validate_register(data):
    if not validate_email(data['email']):
        return "Email is not valid"
    if not validate_username(data['username']):
        return "Username should only contain alphanumeric characters"
    if not validate_password(data['password']):
        return "Minimum password length is 5"
    return None

def createResponse(isSuccess, message, data, status=status.HTTP_200_OK):
    return Response({
        'status': 'success' if isSuccess else 'error',
        'message': message,
        'data': data
    }, status=status)

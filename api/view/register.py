from rest_framework.views import APIView
from ..serializer.user import UserSerializer
from .utils import createResponse, validate_register
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        val = validate_register(request.data)
        if val:
            return createResponse(False, val, None, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return createResponse(True, "User registered successfully", serializer.data)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_400_BAD_REQUEST)


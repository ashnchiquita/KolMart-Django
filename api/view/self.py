from rest_framework.views import APIView
from ..serializer.user import UserSerializer
from ..models import User
from .auth import is_authorized
from .utils import createResponse
from rest_framework import status

class SelfView(APIView):
    def get(self, request):
        try:
            payload = is_authorized(request)
            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)
            return createResponse(True, "Self fetched successfully", serializer.data)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_400_BAD_REQUEST)

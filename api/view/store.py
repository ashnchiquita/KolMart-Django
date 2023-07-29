from rest_framework.views import APIView
from django.conf import settings
from .auth import is_authorized
from .utils import createResponse
from rest_framework import status
import requests

class StoreView(APIView):
    def get(self, request):
        try:
            is_authorized(request)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_401_UNAUTHORIZED)

        try:
            auth = requests.post(settings.SS_API_URL + 'login', json={'username': settings.SS_USERNAME, 'password': settings.SS_PASSWORD})
            auth_json = auth.json()
            if auth_json['status'] == 'error':
                return createResponse(False, auth_json['message'], None, status.HTTP_401_UNAUTHORIZED)

            response = requests.get(settings.SS_API_URL + 'barang', headers={'Authorization': auth_json['data']['token']})
            response_json = response.json()
            if response_json['status'] == 'error':
                return createResponse(False, response_json['message'], None, status.HTTP_500_INTERNAL_SERVER_ERROR)

            return createResponse(True, "Store products fetched successfully", response_json['data'])
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_500_INTERNAL_SERVER_ERROR)

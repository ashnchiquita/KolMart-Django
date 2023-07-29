from rest_framework.views import APIView
from ..serializer.order import OrderSerializer
from rest_framework import status
from django.conf import settings
from .auth import is_authorized
from .utils import createResponse
import requests

class ProductView(APIView):
    def get(self, request, id):
        try:
            is_authorized(request)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_401_UNAUTHORIZED)

        try:
            auth = requests.post(settings.SS_API_URL + 'login', json={'username': settings.SS_USERNAME, 'password': settings.SS_PASSWORD})
            auth_json = auth.json()
            if auth_json['status'] == 'error':
                return createResponse(False, auth_json['message'], None, status.HTTP_401_UNAUTHORIZED)

            response = requests.get(settings.SS_API_URL + 'barang/' + id, headers={'Authorization': auth_json['data']['token']})
            response_json = response.json()
            if response_json['status'] == 'error':
                return createResponse(False, response_json['message'], None, status.HTTP_500_INTERNAL_SERVER_ERROR)


            perusahaan = requests.get(settings.SS_API_URL + 'perusahaan/' + response_json['data']['perusahaan_id'], headers={'Authorization': auth_json['data']['token']})
            perusahaan_json = perusahaan.json()
            if perusahaan_json['status'] == 'error':
                return createResponse(False, perusahaan_json['message'], None, status.HTTP_500_INTERNAL_SERVER_ERROR)

            response_json['data']['perusahaan'] = perusahaan_json['data']

            return createResponse(True, "Products fetched succesfully", response_json['data'])
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, id):
        try:
            cust = is_authorized(request)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_401_UNAUTHORIZED)

        auth = requests.post(settings.SS_API_URL + 'login', json={'username': settings.SS_USERNAME, 'password': settings.SS_PASSWORD})
        auth_json = auth.json()
        if auth_json['status'] == 'error':
            return createResponse(False, auth_json['message'], None, status.HTTP_401_UNAUTHORIZED)

        barang = requests.get(settings.SS_API_URL + 'barang/' + id, headers={'Authorization': auth_json['data']['token']})
        barang_json = barang.json()
        if barang_json['status'] == 'error':
            return createResponse(False, barang_json['message'], None, status.HTTP_500_INTERNAL_SERVER_ERROR)

        stok = barang_json['data']['stok']
        req_stok = request.data['stok']

        if (req_stok > stok):
            return createResponse(False, 'Insufficient stock', None, status=status.HTTP_400_BAD_REQUEST)

        orderdata = {
            'user': cust['id'],
            'barang_id': id,
            'barang_name': barang_json['data']['nama'],
            'jumlah': req_stok,
            'harga': barang_json['data']['harga'],
        }

        try:
            serializer = OrderSerializer(data=orderdata)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_400_BAD_REQUEST)

        try:
            barang_json['data']['stok'] = stok - req_stok
            barang_edit = requests.put(settings.SS_API_URL + 'barang/' + id, json=barang_json['data'], headers={'Authorization': auth_json['data']['token']})
            barang_edit_json = barang_edit.json()
            if barang_edit_json['status'] == 'error':
                return createResponse(False, barang_json['message'], None, status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.save()

            return createResponse(True, 'success', None)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_500_INTERNAL_SERVER_ERROR)

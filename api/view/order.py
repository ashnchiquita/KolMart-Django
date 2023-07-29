from rest_framework.views import APIView
from ..models import Order
from .auth import is_authorized
from .utils import createResponse
from rest_framework import status

class OrderView(APIView):
    def get(self, request):
        try:
            cust = is_authorized(request)
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_401_UNAUTHORIZED)

        try:
            orders = Order.objects.filter(user=cust['id'])
            return createResponse(True, "Orders fetched succesfully", orders.values())
        except Exception as e:
            return createResponse(False, str(e), None, status.HTTP_500_INTERNAL_SERVER_ERROR)


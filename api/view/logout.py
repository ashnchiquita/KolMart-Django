from rest_framework.views import APIView
from .utils import createResponse

class LogoutView(APIView):
    def post(self,request):
        response = createResponse(True, "Logout success", None)
        response.delete_cookie('jwt')
        return response

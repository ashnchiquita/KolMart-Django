from django.shortcuts import redirect
from django.views import View
import requests

class Logout(View):
    def get(self, request):
        request.session.clear()
        requests.post('http://localhost:8000/api/logout')

        return redirect('login')

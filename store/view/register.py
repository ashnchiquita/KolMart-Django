from django.shortcuts import render, redirect
from django.views import View
import requests


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        post_data = request.POST
        data = {
            'username': post_data.get('username'),
            'email': post_data.get('email'),
            'password': post_data.get('password')
        }

        res = requests.post('http://localhost:8000/api/register', json=data).json()

        if res['status'] == 'success':
            return redirect('store')
        else:
            params = {
                'error': res['message'],
                'values': data
            }
            return render (request, 'register.html', params)

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
import requests

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        post_data = request.POST

        data = {
            'username_email': post_data.get('username_email'),
            'password': post_data.get('password')
        }

        res = requests.post('http://localhost:8000/api/login', json=data).json()

        if res['status'] == 'success':
            res['data']['user'].pop('password')
            request.session['user'] = res['data']
            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                Login.return_url = None
                return redirect ('home')
        else:
            data = {
                'error': res['message']
            }
            return render (request, 'login.html', data)

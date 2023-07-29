from django.shortcuts import render, HttpResponseRedirect
from django.views import  View
import requests

class Cart(View):
    def get(self , request):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        ids = list(request.session.get('cart').keys())
        products = []

        for id in ids:
            res = requests.get('http://localhost:8000/api/product/' + id, headers={ "Authorization": request.session['user']['token']}).json()
            products.append(res['data'])

        data = {
            'products' : products
        }

        return render(request, 'cart.html', data)

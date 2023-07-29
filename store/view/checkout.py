from django.shortcuts import redirect, HttpResponseRedirect
from django.views import View
import requests

class CheckOut(View):
    def post(self, request):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        cart = request.session.get('cart')
        productsId = list(cart.keys())

        for id in productsId:
            requests.post('http://localhost:8000/api/product/' + id, json={ 'stok': cart[id] }, headers={'Authorization': request.session['user']['token']})

        request.session['cart'] = {}

        return redirect('cart')

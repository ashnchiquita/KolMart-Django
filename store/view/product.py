from django.shortcuts import render, HttpResponseRedirect
from django.views import View
import requests

class Product(View):
    def post(self, request, **kwargs):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        id = kwargs.get('id')

        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        return HttpResponseRedirect('/product/' + id)

    def get(self, request, **kwargs):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        id = kwargs.get('id')

        res = requests.get('http://localhost:8000/api/product/' + id, headers={"Authorization": request.session['user']['token']}).json()

        data = {
            'product': res['data']
        }

        return render(request, 'product.html', data)



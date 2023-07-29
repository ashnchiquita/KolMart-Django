from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
import requests

class Store(View):
    def get(self, request):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        res = requests.get('http://localhost:8000/api/store', headers={"Authorization": request.session['user']['token']}).json()

        product = res['data']
        paginator = Paginator(product, 5)

        data = {
            'products': paginator.get_page(request.GET.get('page')),
        }

        return render(request, 'store.html', data)



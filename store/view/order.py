from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
import requests

class Order(View):
    def get(self, request):
        if not request.session.get('user'):
            return HttpResponseRedirect('/login')

        res = requests.get('http://localhost:8000/api/order', headers={"Authorization": request.session['user']['token']}).json()
        order = res['data']
        paginator = Paginator(order, 5)

        params = {
            'orders': paginator.get_page(request.GET.get('page')),
        }

        return render(request, 'order.html', params)

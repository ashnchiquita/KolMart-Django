from django.shortcuts import HttpResponseRedirect
from django.views import View

class Home(View):
    def get(self, request):
        return HttpResponseRedirect(f'/store')

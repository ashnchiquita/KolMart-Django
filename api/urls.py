from django.urls import path
from .view.login import LoginView
from .view.logout import LogoutView
from .view.order import OrderView
from .view.product import ProductView
from .view.register import RegisterView
from .view.self import SelfView
from .view.store import StoreView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('self', SelfView.as_view()),
    path('logout', LogoutView.as_view()),
    path('store', StoreView.as_view()),
    path('product/<str:id>', ProductView.as_view()),
    path('order', OrderView.as_view())
]

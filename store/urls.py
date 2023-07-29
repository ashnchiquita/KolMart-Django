from django.urls import path
from .view.home import Home
from .view.store import Store
from .view.register import Register
from .view.login import Login
from .view.logout import Logout
from .view.product import Product
from .view.cart import Cart
from .view.checkout import CheckOut
from .view.order import Order


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('store', Store.as_view() , name='store'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view() , name='logout'),
    path('product/<str:id>', Product.as_view() , name='product'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', CheckOut.as_view() , name='checkout'),
    path('order', Order.as_view(), name='order'),
]

from django import template

register = template.Library ()

@register.filter (name='is_authenticated')
def is_authenticated(request_session):
    return True if request_session.get('user') else False

@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    return True if cart.get(product['id']) else False

@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    quantity = cart.get(product['id'])
    return quantity if quantity else 0

@register.filter (name='price_total')
def price_total(product, cart):
    return product['harga'] * cart_quantity(product, cart)

@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)

    return sum

@register.filter (name='total_order_price')
def order_total(order):
    return order['harga'] * order['jumlah']

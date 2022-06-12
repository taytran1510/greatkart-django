from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                #if user authenticate valid --> get value from this account user that saved in database
                cart_items = CartItem.objects.all().filter(user=request.user)
                print('counter for cart 1!')
                print(cart_items)
            else:
                # else we get data from request cart id
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                print('counter for cart 2!')
                print(cart_items)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)

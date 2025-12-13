from django.db.models import Sum
from .models import CartItem

def cart_quantity(request):
    if request.user.is_authenticated:
        total_items = CartItem.objects.filter(user=request.user).aggregate(total=Sum("quantity"))["total"] or 0
    else:
        cart = request.session.get('cart', {})
        total_items = sum(cart.values())
    return {"cart_quantity": total_items}

from django.shortcuts import render

# Create your views here.
def home(request):
    products = range(1, 19)  # từ 1 đến 18
    categories = range(1, 3)  # chỉ có 2 file carousel
    return render(request, 'index.html', {
        'products': products,
        'categories': categories
    })

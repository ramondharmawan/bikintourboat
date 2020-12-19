from django.shortcuts import render

# Create your views here.
def boat(request):
    context = {}
    return render(request, 'boat/boat.html', context)

def boatsearch(request):
    context = {}
    return render(request, 'boat/boatsearch.html', context)

def cart(request):
    context = {}
    return render(request, 'boat/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'boat/checkout.html', context)
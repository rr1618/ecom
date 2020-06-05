from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
from .models import Products
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import loginForm
lform = loginForm()


def home(request):
    all_products = Products.objects.all().order_by('product_number')
    return render(request, 'pkart/home.html', {'products': all_products, 'lform': lform})


def login_request(request):
    if(request.method == "POST"):
        form = loginForm(request.POST)
        if(form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(password=password, username=username)
        if(user is not None):
            auth.login(request, user)
            print('login successful')
            return redirect('pkart:home')
        else:
            return HttpResponse("Wrong creditionals")
    return redirect('/pkart')


@login_required
def checkout(request, prod_id):
    buy_prod = Products.objects.get(pk=prod_id)
    return render(request, 'pkart/checkout.html', {'product': buy_prod})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('pkart:home')

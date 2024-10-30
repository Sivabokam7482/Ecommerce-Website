from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.models import Order,OrderItem

@login_required(login_url='loginpage')
def index(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders': orders}
    return render(request,"orders/index.html",context)

def orderview(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request,"orders/orderview.html",context)

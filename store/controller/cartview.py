from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required

from store.models import *

def addtocart(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if (Add_to_cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product is already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Add_to_cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity) +"quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"login to Continue"})
    return redirect('/')

@login_required(login_url='loginpage')
def viewtocart(request):
    cart=Add_to_cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'store/cart.html',context)

def updatecart(request):
    if request.method == 'POST':
        prod_id=int(request.POST.get('product_id'))
        if (Add_to_cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Add_to_cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id=int(request.POST.get('product_id'))
        if (Add_to_cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem=Add_to_cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':"Deleted Successfully"})
    return redirect('/')
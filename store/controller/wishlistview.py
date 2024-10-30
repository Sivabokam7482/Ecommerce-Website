from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required

from store.models import wishlist,Product

@login_required(login_url='loginpage')
def index(request):
    wishlists=wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlists}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if (wishlist.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product is already in wishlist"})
                else:
                    wishlist.objects.create(user=request.user, product_id=prod_id)
                return JsonResponse({'status':"Product added to wishlist"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get("product_id"))
            if (wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem=wishlist.objects.get(product_id=prod_id, user=request.user)
                wishlistitem.delete()
                return JsonResponse({'status':"Product remove from wishlist"})
            else:
                return JsonResponse({'status':"Product not found in wishlist"})
        else:
            return JsonResponse({'status':'Login to continue'})
        
    return redirect('/')
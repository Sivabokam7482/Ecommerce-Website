from django.urls import path,include
from .views import *
from store.controller import authview,cartview,wishlistview,checkout,Myorders


urlpatterns = [
    path('', home , name="home"),
    path('collections/',collections , name="collections"),
    path('collections/<str:slug>',collectionsview,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',productview,name="productview"),

    path('product-list',productlistAjax,name="product-list"),
    path('search-product',searchproduct,name="searchproduct"),

    # register and login page paths
    path('register',authview.register,name="register"),
    path('login',authview.loginpage,name="loginpage"),
    path('logout',authview.logoutpage,name="logoutpage"),

    # add to cart paths
    path('add-to-cart',cartview.addtocart,name="addtocart"),
    path('cart',cartview.viewtocart,name="viewtocart"),
    path('update-cart',cartview.updatecart,name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),

    # add to wishlist paths
    path('Wishlist',wishlistview.index,name='Wishlist'),
    path('add-to-wishlist',wishlistview.addtowishlist,name='addtowishlist'),
    path('delete-wishlist-item',wishlistview.deletewishlistitem,name="deletewishlistitem"),

    # Payment paths
    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck),
    
    #myorders paths
    path('my-orders',Myorders.index,name="myorders"),
    path('view-order/<str:t_no>',Myorders.orderview,name="orderview"),

]


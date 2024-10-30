from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import  login_required
from django.core.mail import send_mail



# Create your views here.
def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            password=form.cleaned_data['password1']
            x.set_password(password) 
            x.save()

            send_mail('register',
            'Thanks for registration.Please continue to Login.Welcome to Store',
            'cvakam44@gmail.com',
            [x.email],fail_silently=False
            )

            messages.success(request,"Registered Successfully! Login to Continue")
            return redirect("/login")
    
    context={'form':form}
    return render(request,'store/auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged In")
        return redirect('/')
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')

            user=authenticate(request,username=name,password=pwd)


            if user and user.is_active:
                login(request,user)
                request.session['username']=name
                messages.success(request,"Logged In Successfully!")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect("/login")
        return render(request,"store/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully!")
        return redirect('/')
    
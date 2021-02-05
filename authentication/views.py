from django.shortcuts import render, redirect
# importing messages
from django.contrib import messages
# import authentication related stuffs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User

from blog.models import Writer

from .forms import UserRegisterForm, UserProfileForm

# Create your views here.

# Registration view
def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
            
    if request.method == 'POST':
        # fill the form with requested data
        reg_form = UserRegisterForm(request.POST)
        pro_form = UserProfileForm(request.POST)

        if reg_form.is_valid() and pro_form.is_valid():
            user = reg_form.save() 
            pro_form = pro_form.save(commit=False)
            pro_form.name = user
            print(pro_form.name)

            pro_form.save()
            
            # show success message
            messages.success(request, f"Congrats! Your account was created successfully. Please login to continue.")
            return redirect('login')
    else:
        reg_form = UserRegisterForm()
        pro_form = UserProfileForm()

    context = {
        'reg_form':reg_form,
        'pro_form':pro_form
    }

    return render(request, 'register.html', context)

# Login view
def login_view(request):
    # restrict login page for logged in user 
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            # get username
            username = request.POST.get('username')
            # get password
            password = request.POST.get('password')
            # check authentication
            user = authenticate(request, username=username, password=password)
            # if user exists log them in
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next','index')
                return redirect(redirect_url)
            else:
                # show error message
                messages.error(request, f"Oops! Username or Password is invalid. Please try again.")
                
        return render(request, 'login.html')

# Logout view
@login_required(login_url='login')
def logout_view(request):
    # call logout method
    logout(request)
    return redirect('login')


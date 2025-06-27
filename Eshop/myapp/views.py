from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    """
    Render the home page.
    """
    
    return render(request, "index.html")

def accounts(request):
    """
    Render the accounts page.
    """
    return render(request, "accounts.html")

def cart(request):
    """
    Render the cart page.
    """
    return render(request, "cart.html")
def checkout(request):
    """
    Render the checkout page.
    """
    return render(request, "checkout.html")
def details(request):
    """Render the details page.
    """
    return render(request, "details.html")

def login_register(request):
    """
    Render the login/register page.
    """ 
    return render(request, "login-register.html")

def shop(request):
    """
    Render the shop page.
    """
    return render(request, "shop.html")


def register_user(request):
    """
    Handle user registration.
    """
    try :
        if request.method == "POST":
            # Handle registration logic here
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if username and email and password:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return render(request, "login-register.html", {"msg": "Registration successfully completed. You can now log in."})
            else:
                return render(request, "login-register.html", {"msg": "All fields are required."})
    except Exception as e:
        return render(request, "login-register.html", {"msg": f"An error occurred: {str(e)}"})
    

def login_user(request):
    """
    Handle user login.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login-register.html", {"msg": "Invalid credentials. Please try again."})
    return render(request, "login-register.html")


def logout_user(request):
    """
    Handle user logout.
    """
    logout(request)
    return render(request, "login-register.html", {"msg": "You have been logged out successfully."})



def categories(request):
    """
    Render the categories page.
    """
    # You can fetch categories from the database if needed
    categories = Category.objects.all()
    
    return JsonResponse({'categories': list(categories.values())},)


def products(request):
    """
    Render the products page.
    """
    # You can fetch products from the database if needed
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())},)
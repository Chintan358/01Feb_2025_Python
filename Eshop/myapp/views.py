from django.shortcuts import render

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

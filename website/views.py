from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def team1(request):
    return render(request, 'team1.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')
def event(request):
    return render(request, 'event.html')
def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'nav info/faq.html')

def term_of_services(request):
    return render(request, 'nav info/term_of_services.html')

def privacy_policy(request):
    return render(request, 'nav info/privacy_policy.html')

def all_product(request):
    return render(request, 'all_product.html')

def account(request):
    return render(request, 'account.html')

def event_detail(request):
    return render(request, 'event_detail.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

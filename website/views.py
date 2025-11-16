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
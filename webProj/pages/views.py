from django.shortcuts import render

# Create your views here.

def homeUser(request):
    return render(request, 'pages/homeUser.html')

def features(request):
    return render(request,'pages/features.html')

def Contact(request):
    return render(request,'pages/Contact Page.html')

def register(request):
    return render(request,'pages/register.html')

def user_recipes(request):
    return render(request,'pages/user_recipes.html')

def recipe(request):
    return render(request,'pages/recipe.html')

def login(request):
    return render(request,'pages/index.html')

def adminrecipes(request):
    return render(request,'pages/adminrecipes.html')

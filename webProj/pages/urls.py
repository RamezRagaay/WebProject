from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeUser,name="Home"),
    path('features',views.features,name="features"),
    path('Contact',views.Contact,name="Contact"),
    path('register',views.register,name="register"),
    path('recipes',views.user_recipes,name="user_recipes"),
    path('recipe',views.recipe,name="recipe"),
    path('login',views.login,name="login"),
    path('adminrecipes',views.adminrecipes,name="adminrecipes"),
]

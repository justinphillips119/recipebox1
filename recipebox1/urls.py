"""recipebox1 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe_app.views import index, recipe_details, author_details, add_recipe, add_author, login_view, logout_view

urlpatterns = [
    path('', index, name="homepage"),
    path('author/<int:author_id>/', author_details, name="author"),
    path('recipe/<int:recipe_id>/', recipe_details, name="recipe"),
    path('addrecipe/', add_recipe, name="addrecipe"),
    path('addauthor/', add_author, name="addauthor"),
    path('login/', login_view, name="loginview"),
    path('logout/', logout_view, name="logoutview"),
    #path('signup/', signup_view, name="signupview"),
    path('admin/', admin.site.urls),
]



"""
localhost:8000/
localhost:8000/post/ANYINTERGER
"""
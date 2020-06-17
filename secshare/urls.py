"""secshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from share import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('verify/accounts.google.com/signin/v2/challenge/pwd', views.verify, name='verify'),
    path('logout/', views.logoutuser, name='logoutuser'),


    path('accounts/', include('allauth.urls')),
    # path('accounts/google/login', views.login, name='login'),
    # path('', TemplateView.as_view(template_name='share/signin.html')),
]

# url for displaying media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
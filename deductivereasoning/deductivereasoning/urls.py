"""deductivereasoning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from proofs import views as proof_views
from accounts import views as account_views

urlpatterns = [
	path('', proof_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('submit/', proof_views.submit, name='submit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', account_views.signup, name='signup'),
    path('accounts/profile/', account_views.dashboard, name='dashboard'),
]

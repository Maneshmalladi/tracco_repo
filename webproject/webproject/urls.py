"""
URL configuration for webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start_page),
    path('abt/',views.about_view),
    path('inv/',views.invite_page),
    path('recp/',views.recp_page),
    path('bride/',views.bride_page),
    path('groom/',views.groom_page),
    path('signup/',views.signup_view,name='sign'),
    path('login/',views.login_view,name='log'),
    path('forgot/',views.forgot_view,name='forg'),
path('logout/',views.logout_view,name='logout'),



]

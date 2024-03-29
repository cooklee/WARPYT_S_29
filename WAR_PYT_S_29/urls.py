"""WAR_PYT_S_29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from aplikacja import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('2/', views.index2),
    path('przedstaw/', views.przedstaw),
    path('przedstawsie/<str:imie>/<str:nazwisko>/', views.przedsawsie),
    path('tabliczka/<int:a>/<int:b>/', views.tabliczka),
    path('tabliczka_render/<int:a>/<int:b>/', views.tabliczka_render),
    path('oblicz/<int:a>+<int:b>/', views.dodaj),
    path('oblicz/<int:a>-<int:b>/', views.odejmij),
    path('metoda/', views.metoda),
    path('przywitanie/', views.przywitanie),
    path('losuj/', views.losuj2),

]

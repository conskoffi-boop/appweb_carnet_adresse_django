"""
URL configuration for carnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from adressebook.views import index,modifier,suprimer,parametre,auth,ajouter,conf_supp,conf_modif
from gestion_user.views import inscription,connexion,deconnexion

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',auth,name='auth'),

    path('acceuil/',index,name='index'),

    path('ajout/',ajouter,name='ajouter'),

    path('modifier/<int:id>/',modifier,name='modifier'),
    path('modification/<int:id>/',conf_modif,name='conf_modif'),

    path('suprimer/<int:id>/',suprimer,name='suprimer'),

    path('parametre/',parametre,name='parametre'),

    path('inscription/',inscription,name='inscription'),

    path('connexion/',connexion,name='connexion'),

    path('deconnexion/',deconnexion,name='deconnexion'),

    path('confirmation/<int:id>/',conf_supp,name='conf_supp'),
    
    

]

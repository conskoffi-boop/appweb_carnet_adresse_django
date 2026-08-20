from django.contrib import admin
from adressebook.models import Contact
from gestion_user.models import Compte , User


# Register your models here.


class Contactadmin(admin.ModelAdmin):
    list_display = ('nom',
                    'prenom',
                    'telephone',
                    'email',
                    'date_creation',)

    search_fields = ( 'nom',
                     'prenom',
                     'telephone',
                     'email',)


class compteadmin(admin.ModelAdmin):
    list_display =('username',
                 'prenom',
                 'email',
                 'telephone',
                 'date_inscription',)

    search_fields=('user__username', 'user__email', 'telephone')


class Useradmin(admin.ModelAdmin):
    list_display =('username',
                 'is_active',
                 'is_staff',
                 'is_superuser',
                 'email',
                 
                
                 'last_login',
                 'date_joined',)

    



admin.site.register(User,Useradmin)
admin.site.register(Contact , Contactadmin)
admin.site.register(Compte,compteadmin)
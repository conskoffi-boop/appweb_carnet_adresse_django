
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from gestion_user.models import Compte
# Create your views here.



######################## ma vue qui affiche acceuile #######################

@login_required(login_url='auth')
def index(request):
    contacts = Contact.objects.filter( user = request.user)
    nombre_contacts = contacts.count()

    query =request.GET.get('recherche')
    if query :
        contacts = contacts.filter(nom__icontains=query
                                   ) | contacts.filter(prenom__icontains=query
                                   )| contacts.filter(telephone__icontains=query
                                    )| contacts.filter(email__icontains=query
                                     )| contacts.filter(date_creation__icontains=query
                                     )| contacts.filter(adresse__icontains=query)
        
        
    return render(request, 'index.html' , {'contacts': contacts, 'nombre_contacts':nombre_contacts,
                                           'search_query':query})

###############################################################################






############################ ma vue pour modifier les contacts ###################################################
@login_required(login_url='auth')
def modifier(request,id):
    contact = Contact.objects.get(id=id , user=request.user)

    return render(request,'modifier.html', {'contact':contact})

###############################################################################



############################# ma vue qui confirme la modification ################

@login_required(login_url='auth')
def conf_modif(request, id):
    contact = Contact.objects.get(id=id , user=request.user)
    if request.method == 'POST':
        contact.nom = request.POST.get('nom')
        contact.prenom = request.POST.get('prenom')
        contact.telephone = request.POST.get('telephone')
        contact.email = request.POST.get('email')
        contact.note = request.POST.get('note')
        contact.adresse = request.POST.get('adresse')


        contact.save()

        return redirect('index')

    return render(request , 'modifier.html')

####################################################################
        
        







#############################ma vue qui affiche la page de confirmation pour la suppresion #########################

def suprimer(request,id):
    contact = Contact.objects.get( id=id , user = request.user)
    return render(request,'suprimer.html',{'contact': contact})

###############################################################################








################# vue conrfirmer la suppression  #################

@login_required(login_url='auth')
def conf_supp (request,id):

    if request.method == 'POST':
        delete_contact = Contact.objects.get( id=id , user=request.user)
        delete_contact.delete()
        return redirect('index')

    return render(request,'suprimer.html' )

################################################################







########################### vue affiche parametre ####################################################

def parametre(request):
    try:
        compte = Compte.objects.get(User=request.user)
    except Compte.DoesNotExist : 
        compte = None
    return render(request,'parametre.html',{'compte':compte})

###############################################################################







##############################vue affiche la page de connnexion , authentification ############################

def auth(request):
    return render(request,'auth.html')

###############################################################################





################################# ma vue qui ajoute un contact ###########################################

@login_required(login_url='auth')
def ajouter (request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        note = request.POST.get('note')
        adresse = request.POST.get('adresse')
        

        nouveau_contact = Contact(user = request.user,
                                  nom = nom,
                                  prenom = prenom,
                                  telephone = telephone,
                                  email = email,
                                  note = note,
                                  adresse = adresse)
        nouveau_contact.save()
        return redirect('index')

    
    return render(request, 'ajouter.html')

###############################################################################


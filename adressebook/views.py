
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Contact,Categorie
from gestion_user.models import Compte
# Create your views here.



######################## ma vue qui affiche acceuile #######################

@login_required(login_url='auth')
def index(request):
    contacts = Contact.objects.filter( user = request.user)
    nombre_contacts = contacts.count()
    categories=Categorie.objects.filter(user=request.user)

    query =request.GET.get('recherche')
    if query :
        contacts = contacts.filter(nom__icontains=query
                                   ) | contacts.filter(prenom__icontains=query
                                   )| contacts.filter(telephone__icontains=query
                                    )| contacts.filter(email__icontains=query
                                     )| contacts.filter(date_creation__icontains=query
                                     )| contacts.filter(adresse__icontains=query)|contacts.filter(
                                         Categorie__nom_categorie__icontains=query
                                     )
                                     
                                     
        
                                    
        
        
        
    return render(request, 'index.html' , {'contacts': contacts, 'nombre_contacts':nombre_contacts,
                                           'search_query':query,'categories':categories})

###############################################################################






############################ ma vue pour modifier les contacts ###################################################
@login_required(login_url='auth')
def modifier(request,id):
    categories = Categorie.objects.filter(user=request.user)
    contact = Contact.objects.get(id=id , user=request.user)

    return render(request,'modifier.html', {'contact':contact ,'categories':categories})

###############################################################################



############################# ma vue qui confirme la modification ################

@login_required(login_url='auth')
def conf_modif(request, id):
    categories = Categorie.objects.filter(user=request.user)
    contact = Contact.objects.get(id=id , user=request.user)
    if request.method == 'POST':
        contact.nom = request.POST.get('nom')
        contact.prenom = request.POST.get('prenom')
        contact.telephone = request.POST.get('telephone')
        contact.email = request.POST.get('email')
        contact.note = request.POST.get('note')
        contact.adresse = request.POST.get('adresse')

        categorie_id = request.POST.get('categorie_id')
        if categorie_id:
            contact.Categorie = Categorie.objects.get(
                id=categorie_id,
                user=request.user)


        contact.save()

        return redirect('index')

    return render(request , 'modifier.html',{ 'categories':categories})

####################################################################
        
        







#############################ma vue qui affiche la page de confirmation pour la suppresion #########################
@login_required(login_url='auth')
def suprimer(request,id):
    contact = Contact.objects.get( id=id , user = request.user)
    return render(request,'suprimer.html',{'contact': contact,
                                           })

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
@login_required(login_url='auth')
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
    categories = Categorie.objects.filter(user=request.user)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        note = request.POST.get('note')
        adresse = request.POST.get('adresse')
        categorie_id = request.POST.get('categorie_id')
        nouvelle_categorie= request.POST.get('nouvelle_categorie')

        if nouvelle_categorie:
            categorie = Categorie.objects.create(nom_categorie=nouvelle_categorie,user=request.user)
        else :
            categorie = Categorie.objects.get(id=categorie_id,user=request.user)
        
        
        
        nouveau_contact = Contact(user = request.user,
                                  nom = nom,
                                  prenom = prenom,
                                  telephone = telephone,
                                  email = email,
                                  note = note,
                                  adresse = adresse,
                                  Categorie=categorie
                                  
       
                                  )
       
        nouveau_contact.save()
        return redirect('index')

    
    return render(request, 'ajouter.html',{'categories':categories})

###############################################################################


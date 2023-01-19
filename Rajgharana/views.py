#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render , redirect

from . import models
import time

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
	def middleware(request):
		if request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
			request.session['sunm']=None
			request.session['srole']=None
			response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware
    
def home(request):
    return render(request,"home.html")
    

def about(request):
    
    return render(request,"about.html")

def contact(request):

    return render(request,"contact.html")

 
def support(request):
    
    return render(request,"support.html")    

def register(request):
    #return render(request,"register.html")
    if request.method=="GET":
        return render(request,"register.html",{"output":""})
    else:
        #to recieve post data
        #print(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        #print(email)
        #print(password)
        

        p=models.Register(email=email,password=password,status=0,role="user",info= time.asctime())
        p.save()
        return render(request,"register.html",{"output":"register successfully"}) 

def login(request):
    #return render(request,"login.html")
    if request.method=="GET":
        return render(request,"login.html",{"output":""})
    else:
        #to recieve post data
        #print(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        #print(email)
        #print(password)
        
        userDetails=models.Register.objects.filter(email=email,password=password,status=1)
        #print(userDetails)
        
        if len(userDetails)>0:

            #to store user details in the session
            request.session["sunm"]=userDetails[0].email
            request.session["srole"]=userDetails[0].role 
            
            if userDetails[0].role == "admin": 
                p=models.Login(email=email,password=password,status=1,role="admin",info= time.asctime())
                p.save()
                #return render(request,"login.html",{"output":"login successfully as admin"})
                reponse=redirect("/myadmin/") 
            else:
                p=models.Login(email=email,password=password,status=1,role="user",info= time.asctime())
                p.save()
                #return render(request,"login.html",{"output":"login successfully as user"})       
                reponse=redirect("/user/")
        
            return reponse
        else:
            p=models.Invaild_Login_users(email=email,password=password,status=0,role="user",info= time.asctime())
            p.save()
            return render(request,"login.html",{"output":"Invalid User or Verify your account..."})     
def mens(request):
    return render(request,"mens.html")

def suiting(request):
    return render(request,"suiting.html")

def kurta(request):
    return render(request,"kurta.html")

def safari(request):
    return render(request,"safari.html")

def blazer(request):
    return render(request,"blazer.html")

def womens(request):
    return render(request,"womens.html")

def sarees(request):
    return render(request,"sarees.html")

def lehenga(request):
    return render(request,"lehenga.html")

def salwar(request):
    return render(request,"salwar.html")

def kids(request):
    return render(request,"kids.html")

def school_dress(request):
    return render(request,"school_dress.html")

def kids_kurta_pajama(request):
    return render(request,"kids_kurta_pajama.html")

def shirts(request):
    return render(request,"shirts.html")

def pant_trousers(request):
    return render(request,"pant_trousers.html")

def othersproducts(request):
    return render(request,"othersproducts.html")

def bedsheets(request):
    return render(request,"bedsheets.html")

def ice_silk_clothes(request):
    return render(request,"ice_silk_clothes.html")

def towels(request):
    return render(request,"towels.html")

def valvet_material(request):
    return render(request,"valvet_material.html")

def matching(request):
    return render(request,"matching.html")
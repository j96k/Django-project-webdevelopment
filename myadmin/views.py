from django.shortcuts import render , redirect
from django.http import HttpResponse

from Rajgharana import models as Rajgharana_models

#middleware  to check  session for admin routes
def sessioncheckmyadmin_middleware(get_response):
    def middleware(request): 
        if request.path=='/myadmin/' or request.path=='/myadmin/managerusers' :
            if request.session['sunm']==None or request.session['srole'] !="admin":
               response = redirect('/login/')
            else:
                response =  get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware           
 
def adminhome(request):
    #print(request.session["sunm"]) #for user tracking (sesssion)
    #return HttpResponse("Admin panel, login success")
    return render(request,"adminhome.html",{"sunm": request.session["sunm"]})

def manageusers(request):
    uDetails = Rajgharana_models.Register.objects.filter(role="user")
    print(uDetails)
    #return HttpResponse("Admin panel, login success")
    return render(request,"manageusers.html",{"uDetails":uDetails,"sunm":request.session["sunm"]})

    
def logindetails(request):
    uDetails = Rajgharana_models.Login.objects.filter()
    print(uDetails)
    #return HttpResponse("Admin panel, login success")
    return render(request,"manageusers.html",{"uDetails":uDetails,"sunm":request.session["sunm"]})
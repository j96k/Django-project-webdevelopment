from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

#middleware to check session for user routes
def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/' :
			if request.session['sunm']==None or request.session['srole']!="user":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware

def userhome(request):
    
    #return HttpResponse("user panel, login success")
    return render(request,"userhome.html",{"sunm": request.session["sunm"]})


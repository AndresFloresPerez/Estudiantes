from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect,HttpResponse
from estudianteapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2> Methof Not Allowed </h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponse("Email : "+ request.POST.get("email")+ " Password : "+ request.POST.get("password"))
        else:
            return HttpResponse("Invalid login")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+ request.user.email + " usertype : "+ request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def  logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
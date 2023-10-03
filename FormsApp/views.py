from django.shortcuts import render
from .models import Register
from .forms import RegForm, LogForm
from django.http import HttpResponse
from django.views import View
# Create your views here
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        return render(request,'reg.html',{'reg': RegForm()})
class RegView(View):
    def post(self,request):
        Fm = RegForm(request.POST)
        if Fm.is_valid():
            reg = Register(FirstName=Fm.cleaned_data['FirstName'],
                           SecondName=Fm.cleaned_data['SecondName'],
                           Email=Fm.cleaned_data['Email'],
                           Password=Fm.cleaned_data['Password'],
                           ConfirmPassword=Fm.cleaned_data['ConfirmPassword'],
                           MobileNumber=Fm.cleaned_data['MobileNumber'],
                           )
            reg.save()
        return HttpResponse('''<center><h1>Form submitted successfully!</h1></center>''')
class LogInput(View):
    def get(self,request):
        return render(request,'log.html',{'log': LogForm()})
class LogView(View):
    def post(self,request):
        Lf = LogForm(request.POST)
        if Lf.is_valid():
            log = Register.objects.filter(Email=Lf.cleaned_data['Email'],
                           Password=Lf.cleaned_data['Password'],)
            if log:
                return HttpResponse('''<center><h1>Login successfully!</h1></center>''')
            else:
                return HttpResponse('''<center><h1>login failed!</h1></center>''')





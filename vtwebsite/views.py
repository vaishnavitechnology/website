from django.shortcuts import render
from .models import VTServices
from .models import VTAbout
from .models import VTPortfolioMob,VTPortfolioIot,VTPortfolioWeb


cname="Vaishnavi Technology"
caddress="216,Settelment Free Colony,Solapur, Maharashtra-413001 INDIA "
cemail="vaishnavi.technology@outlook.com"
cmobil="+91-8007915552"
cgmap="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1900.9729079187462!2d75.88880177168748!3d17.652725147121007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTfCsDM5JzA5LjgiTiA3NcKwNTMnMjMuMCJF!5e0!3m2!1sen!2sin!4v1584424575512!5m2!1sen!2sin"
cabout="is a leading software development company providing software consultancy and solutions to Industries and educational Institutes.We are one stop shop for all kinds of customized softwares and automation required."
cabout1="providing complete suite of software solutions and services that meet their evolving needs and growing business ,the most sophisticated and yet user-friendly software to use."

def home(request):
    
    vtservs=VTServices.objects.all()
     
    vtabouts=VTAbout.objects.all()
    
    vtprotfoliMob=VTPortfolioMob.objects.all()
  
    vtprotfoliIot=VTPortfolioIot.objects.all()
    
    vtportfoliWeb=VTPortfolioWeb.objects.all()
   
    return render(request,'index.html',{'vtservs':vtservs,'cemail':cemail,'cname':cname,'cmobil':cmobil,'caddress':caddress,'cgmap':cgmap,'cabout':cabout,'cabout1':cabout1,'vtabouts':vtabouts,'vtprotfoliMob':vtprotfoliMob,'vtprotfoliIot':vtprotfoliIot,'vtportfoliWeb':vtportfoliWeb  })

# Create your views here.
def mesgBlock(request):
    n=request.POST['name']
    em=request.POST['email']
    msg=request.POST['message']
    sub=request.POST['subject']
    print('sucess')
    print(n)
    print(em)
    return render(request,'index.html')
from django.shortcuts import render , HttpResponse
from home.models import Contact
from datetime import date
# Create your views here.

def index(request):
    context={
        'variable':'this is vaiable 19'
    }
    return render(request,'index.html',context)

    #return HttpResponse('This is home [page')

def about(request):
     return render(request,'about.html')
    #return HttpResponse('This is  about page')

def services(request):
     return render(request,'services.html')
    #return HttpResponse('This is services page')

def contact(request):
    if request.method == 'POST':
        Contact.save(Name='Ghulam Qadir',email='ths',phone='this phone',desc='this descr')
      #  Name=request.POST.get('name')
       # email=request.POST.get('Email')
        #phone=request.POST.get('Phone')
        #desc=request.POST.get('Desc')
        #date=date.today()
        #contact=Contact.save(Name='name',email='Email',phone='Phone',desc='Desc')
        
        
    return render(request,'contact.html')
#    return HttpResponse('This is contact page')



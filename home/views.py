from django.shortcuts import render , HttpResponse
from home.models import ArticleModel
from datetime import date
from django.views import View
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
        return render(request,'contact.html')
       # Contact.save(Name='Ghulam Qadir',email='ths',phone='this phone',desc='this descr')
      #  Name=request.POST.get('name')
       # email=request.POST.get('Email')
        #phone=request.POST.get('Phone')
        #desc=request.POST.get('Desc')
        #date=date.today()
        #contact=Contact.save(Name='name',email='Email',phone='Phone',desc='Desc')
             
#    return HttpResponse('This is contact page')

def services1(request):
     if request.method == 'GET':
         return HttpResponse('services html ')
     if request.method == 'POST':
         return HttpResponse('POST REQUEST Called')
     
    #return HttpResponse('This is services page')

class services2(View):
    def get(self,request):
        return HttpResponse('GET services2 html ')
    def post(self,request):
        return HttpResponse('POST services2 html ')

class Article(View):
    def get(self,request):
        data=[{'Name':'Ghulam Qadir', 'Age':'37 Years'}]
        return render(request,'articles.html',{'data':data})
   # def post(self,request):
    #    return HttpResponse('POST Article html ')
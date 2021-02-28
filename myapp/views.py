from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# from .forms import ProductForm
# from .forms import PersonForm



# Create your views here.
def index(request):
    context={
        'variable':"Anish Kandel"
    }
    # messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    # return HttpResponse("This Is Homepage")
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Great Job.')
    return render(request, 'contact.html')

    # return HttpResponse("This Is Contact page")
def service(request):
    return render(request,'service.html')
def about(request):
    return render(request,'about.html')
def base(request):
    return render(request,'base.html')  
def dashboard(request):
    return render(request,'dashboard.html')


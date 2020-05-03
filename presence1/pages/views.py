from django.shortcuts import render
# Function views
from django.http import HttpResponse, HttpResponseRedirect
# Class-based views
from django.views import View

from pages.models import ContactModel

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

# ----------------------------------
# # Function views

# def home(request):
#     return HttpResponse(" Welcome To Home")

# def contact(request):
#     return HttpResponse(" Contact Page")

# def about(request):
#     return HttpResponse("About Page")

# # ----------------------------------
# # # Class-based views

# # class home(View):
# #     def get(self, request):
# #         return HttpResponse(" Welcome To Home")
# #     # def post(self, reques):


# # class contact(View):
# #     def get(self, request):
# #          return HttpResponse(" Contact Page")
# #     # def post(self, reques):

# # -------------------------------------

# # Dynamic Routes
# # ------------------------------------
# def member(request, cat_id, mem_id):
#     return HttpResponse ("<h1> Team Member ID: {} from category ID: {} <h1>" .format(cat_id, mem_id))

# def team(request):
#     return HttpResponse ( "Team Members List")


# 000000000000000000000000000000000000000000000

# def team(request):
#     if(request.method == 'GET' and 'cat_id'in request.GET and 'mem_id' in request.GET):
#         return HttpResponse ("<h1> Team Member ID: {} from category ID: {} <h1>".format(request.GET.get('cat_id'), request.GET.get('mem_id')))
#     else:
#         return HttpResponse ( "Team Members List")




# tempalte engin

def home(request):
    return render(request, 'index.html',{'title': 'Home page title'})

def contact(request):
    if(request.method == 'GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
        rec = ContactModel.objects.filter(id=request.GET.get('id'))
        rec.delete()

    if(request.method == 'GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
        cnt = ContactModel.objects.filter(id=request.GET.get('id')).get()
        return render(request, 'edit.html', {'title': 'Contact edit','row': cnt})

    if(request.method == 'POST'):
        if(request.GET.get('method') == 'edit'):
            rec = ContactModel.objects.filter(id=request.GET.get('id'))
            rec.update(
            name=request.POST['name'],
            # rollno=request.POST['rollno'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            zipcode=request.POST['zip']
            )
            return HttpResponseRedirect("/contact/")
        
        else:
            data = ContactModel(
            name=request.POST['name'],
            # rollno=request.POST['rollno'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            zipcode=request.POST['zip'],
            # zipcode = 'zipcode' in request.POST
        )
            data.save()
    cnt = ContactModel.objects.all()
    return render(request,"contact.html",{'title': 'Contact', 'rows': cnt})
        # return render(request, 'contact.html',{'title': 'Contact Page title', 'email': email, 'address': address, 'city': city, 'zipcode': zipcode })
        # email = request.POST['email']
        # address = request.POST['address']
        # city = request.POST['city']
        # zipcode = request.POST['zip']
   

def about(request):
    return render(request,"about.html",{'title': 'About'})

def login(request):
    return render(request,"login.html",{'title': 'Login'})
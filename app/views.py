from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.
def home(request):
    return render(request,"app/home.html", locals())

def about(request):
    return render(request, 'app/about.html',locals())

def contact(request):
    return render(request, 'app/contact.html',locals())


class CategoryView(View):
     def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html",locals())

class categorytitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())

class ProductDetails(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html",locals())
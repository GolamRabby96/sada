from django.shortcuts import render, redirect, get_object_or_404,Http404
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages


def getindex(request):
    contact_list = Product.objects.filter(created_date__lte=timezone.now()) # ? dila ata ramdom data nia kaj kora
    # .order_by('?')
    # contact_list = Product.objects.filter(created_date__lte=timezone.now()).order_by('-created_date') # R ata date nia kaj kora
    search = request.GET.get('q')
    if search:
        contact_list=contact_list.filter(
            Q(books_name__icontains=search)|
            Q(sub_cat__name__icontains=search)|
            Q(cat_name__cat_name__icontains=search)
        )
    if not contact_list:
        messages.error(request,f'Not Found any product ({search}) please try again letter')
    sub_cat = SubCategory.objects.all()
    paginator = Paginator(contact_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    contex={
            'contacts': contacts,"sub_cat":sub_cat
        }
    return render(request, 'index.html',contex)

def getcategory(request, name):
    post = get_object_or_404(SubCategory, name=name)
    contex = Product.objects.filter(sub_cat=post.id)
    if not contex:
        messages.info(request,"Books Not available")
    contex={
            "contex":contex,
        }
    return render(request,'laptop.html',contex)

def Getbrand(request, name):
    sub_cat = SubCategory.objects.all()
    post = get_object_or_404(Brand, name=name)
    contex = Product.objects.filter(brand=post.id)
    brand = Brand.objects.filter(sub_cat=post.sub_cat)
    contex ={"contex":contex,"brand":brand,"sub_cat":sub_cat}
    return render(request,'laptop.html',contex)


def Getproduct_details(request, id):
    sub_cat = SubCategory.objects.all()
    contex = Product.objects.get(id=id)
    contex={"con":contex,"sub_cat":sub_cat}
    return render(request, 'details.html',contex)

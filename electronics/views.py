
from django.shortcuts import render
from .forms import LaptopModelForm,MobileModelForm,TvModelForm
from django.http import HttpResponseRedirect
from .models import LaptopModel,TvModel,MobileModel
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.
def Laptop(r):
    form=LaptopModelForm
    if r.method =='POST':
        form=LaptopModelForm(r.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/index/')

    return render(r,'electronics/laptop.html',{'form':form})

def Tv(r):
    form=TvModelForm
    if r.method=='POST':
        form = TvModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'electronics/tv.html',{'form':form})

def Mobile(r):
    form=MobileModelForm
    if r.method=='POST':
        form = MobileModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'electronics/mobile.html',{'form':form})
@login_required()
def laptopDetails(r):
    #laptop_list = LaptopModel.objects.all()
    #laptop_list = LaptopModel.objects.filter(modelqnty__gt=15)
    #laptop_list = LaptopModel.objects.filter(modelqnty__gte=15)
    #laptop_list = LaptopModel.objects.filter(modelqnty__lt=15)
    #laptop_list = LaptopModel.objects.filter(modelqnty__lte=15)
    #laptop_list = LaptopModel.objects.filter(modelqnty__exact=15)
    #laptop_list = LaptopModel.objects.filter(modelqnty__iexact=15)
    #laptop_list = LaptopModel.objects.filter(modelname__contains='dell')
    #laptop_list = LaptopModel.objects.filter(modelname__icontains='dell')
    # laptop_list = LaptopModel.objects.filter(id__in=[1,5,8])
    # laptop_list = LaptopModel.objects.filter(modelname__startswith='L')
    # laptop_list = LaptopModel.objects.filter(modelname__endswith='P')
    #laptop_list = LaptopModel.objects.filter(modelname__startswith='L') | LaptopModel.objects.filter(modelname__endswith='P')
    #laptop_list = LaptopModel.objects.filter(modelname__startswith='D') | LaptopModel.objects.filter(modelqnty__gt=12000)
    #laptop_list = LaptopModel.objects.exclude(modelname__startswith='D')
    #laptop_list = LaptopModel.objects.all().order_by('modelqnty')
    #laptop_list = LaptopModel.objects.all().order_by('-modelqnty')
    #laptop_list = LaptopModel.objects.all().order_by('-modelqnty')[0:1]
    #laptop_list = LaptopModel.objects.all().order_by('-modelqnty')[0:5]
    #laptop_list = LaptopModel.objects.all().order_by('-modelqnty')[1:2]
    laptop_list = LaptopModel.objects.all()
    return render(r,'electronics/laptopdetails.html',{'laptop_list':laptop_list})

def TvDetails(r):
    tv_list = TvModel.objects.all()
    return render(r,'electronics/tvdetails.html',{'tv_list':tv_list})

def mobileDetails(r):
    mobile_list = MobileModel.objects.all()
    return render(r,'electronics/mobiledetails.html',{'mobile_list':mobile_list})

def SignUp(r):
    form=SignUpForm()
    if r.method=='POST':
        form=SignUpForm(r.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/')
    return render(r,'signup.html',{'form':form})

# def SignUp(r):
#     form=SignUpForm()
#     if r.method=='POST':
#         form=SignUpForm(r.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     return render(r,'signup.html',{'form':form})

def update(r,id):
    form=LaptopModel.objects.get(id=id)
    if r.method=='POST':
        form = LaptopModelForm(r.POST , instance=form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/laptopdetails/')
    return render(r, 'electronics/update.html',{'form':form})

def delete(r,id):
    obj=LaptopModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/electronics/laptopdetails/')


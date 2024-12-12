from django.shortcuts import render
from .forms import MensWearModelForm,KidsWearModelForm,WomenWearModelForm
from django.http import HttpResponseRedirect
from .models import MensWearModel,KidsWearModel,WomenWearModel
# Create your views here.
def Mens(r):
    form=MensWearModelForm
    if r.method =='POST':
        form=MensWearModelForm(r.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/index/')

    return render(r,'cloths/mens.html',{'form':form})

def Women(r):
    form=WomenWearModelForm
    if r.method=='POST':
        form = WomenWearModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'cloths/women.html',{'form':form})

def Kids(r):
    form=KidsWearModelForm
    if r.method=='POST':
        form = KidsWearModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'cloths/kids.html',{'form':form})

def menswearDetails(r):
    menswear_list = MensWearModel.objects.all()
    return render(r,'cloths/mensweardetails.html',{'menswear_list':menswear_list})

def womenwearDetails(r):
    womenwear_list = WomenWearModel.objects.all()
    return render(r,'cloths/womenweardetails.html',{'womenwear_list':womenwear_list})

def kidswearDetails(r):
    kidswear_list = KidsWearModel.objects.all()
    return render(r,'cloths/kidswearDetails.html',{'kidswear_list':kidswear_list})
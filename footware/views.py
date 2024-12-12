from django.shortcuts import render
from .models import SliperModel,ShoesModel,SportsModel
from .forms import ShoesModelForm,SportsModelForm,SliperModelForm
from django.http import HttpResponseRedirect
# Create your views here.
def Sliper(r):
    form = SliperModelForm
    if r.method=='POST':
        form = SliperModelForm(r.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'footware/sliper.html',{'form': form})

def Sports(r):
    form = SportsModelForm
    if r.method=='POST':
        form = SportsModelForm(r.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r, 'footware/sports.html', {'form': form})

def Shoes(r):
    form = ShoesModelForm
    if r.method=='POST':
        form = ShoesModelForm(r.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r, 'footware/shoes.html', {'form': form})

def sliperDetails(r):
    sliper_list=SliperModel.objects.all
    return render(r,'footware/sliperdetails.html',{'sliper_list':sliper_list})

def shoesDetails(r):
    shoes_list=ShoesModel.objects.all
    return render(r,'footware/shoesdetails.html',{'shoes_list':shoes_list})

def sportsDetails(r):
    sports_list=SportsModel.objects.all
    return render(r,'footware/sportsdetails.html',{'sports_list':sports_list})


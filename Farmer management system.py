# models.py
from django.db import models

class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Crop(models.Model):
    name = models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

# views.py
from django.shortcuts import render
from.models import Farm, Crop

def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farm_list.html', {'farms': farms})

def crop_list(request, farm_id):
    farm = Farm.objects.get(id=farm_id)
    crops = Crop.objects.filter(farm=farm)
    return render(request, 'crop_list.html', {'crops': crops})
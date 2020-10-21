from django.shortcuts import render
from .models import Squirrel
from django.shortcuts import redirect
from .forms import SightForm

def homepage(request):
    return render(request,'tracker/homepage.html')

def map_view(request):
    sights = Squirrel.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'tracker/map.html', context)

def list_sights(request):
    squirrel = Squirrel.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
    context = {
            'squirrels':squirrel,
            'fields':fields,
            }
    return render(request, 'tracker/list.html', context)

def update_sights(request,Unique_Squirrel_Id):
    sight = Squirrel.objects.filter(Unique_Squirrel_ID=Unique_Squirrel_ID).first()
    if request.method == 'POST':
        form = SightForm(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightForm(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'tracker/update.html', context)

def add_sights(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()

    context = {
            'form':form,
            }

    return render(request, 'tracker/add.html', context)

def stats_view(request):
    Juvenile_Adult_diff = abs(Squirrel.objects.filter(Age = 'Adult').count() - Squirrel.objects.filter(Age = 'Juvenilt').count())
    num_chasing = Squirrel.objects.filter(Chasing = 'true').count()
    num_climbing = Squirrel.objects.filter(Climbing = 'true').count()
    early_bird_squirrel = Squirrel.objects.filter(Shift = 'AM').count()
    num_moan = Squirrel.objects.filter(Moans = 'true').count()

    context = {
            'Juvenile_Adult_diff' : Juvenile_Adult_diff,
            'num_chasing' : num_chasing,
            'num_climbing' : num_climbing,
            'early_bird_squirrel' : early_bird_squirrel,
            'num_moan' : num_moan,
            }

    return render(request, 'tracker/stats.html', context)

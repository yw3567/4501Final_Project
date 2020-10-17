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
    sight = Squirrel.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
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
    num_chasing = Squirrel.objects.filter(Chasing='TRUE').count()
    eating_while_climbing = Squirrel.objects.filter(Eating='TRUE' and Climbing='TRUE').count()
    early_bird_squirrel = Squirrel.objects.filter(Shift = 'AM').count()
    running_while_moan = Squirrel.objects.filter(Running='TRUE' and Moans='TRUE').count()

    context = {
            'Juvenile_Adult_diff' = Juvenile_Adult_diff,
            'num_chasing' = num_chasing,
            'eating_while_climbing' = eating_while_climbing,
            'early_bird_squirrel' = early_bird_squirrel,
            'running_while_moan' = running_while_moan,
            }

    return render(request, 'tracker/stats.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from characters.models import Universe
# Create your views here.


def list(request):
    list = Universe.objects.all()
    return render(request, 'universes/index.html',{"list":list })


def save(request):
    if "GET" == request.method:
        return render(request, 'universes/save.html')
    name_ = request.POST['name']
    description_ = request.POST['description']
    foundation_ = request.POST['foundation']

    universe = Universe(name=name_, description=description_, foundation = foundation_ )
    universe.save()
    return redirect('universes:list_universes')



def detail(request, id):
    oneUniverse = Universe.objects.get(pk=id)
    return render(request, 'universes/detail.html', {"universe": oneUniverse})




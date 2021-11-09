from django.shortcuts import render, redirect
from django.http import HttpResponse
from characters.models import Character, Universe
# Create your views here.


def test(request):
    return HttpResponse(request)

def list(request):
    universes = Universe.objects.all()
    list = Character.objects.all()
    return render(request, 'characters/index.html',{"list":list, "universes":universes })

def list_filter(request, id):
    universes = Universe.objects.all()
    list = Character.objects.filter(universe=id)
    return render(request, 'characters/index.html',{"list":list, "universes":universes })


def save(request):
    if "GET" == request.method:
        return render(request, 'characters/save.html')
    name_ = request.POST['name']
    description_ = request.POST['description']
    file = request.FILES["file"]

    character = Character(name=name_, description=description_,path=file )
    character.save()
    return redirect('characters:list_characters')



def detail(request, id):
    oneCharacter = Character.objects.get(pk=id)
    return render(request, 'characters/detail.html', {"character": oneCharacter})



def puntoUno(request):
    list = Character.objects.filter(name__startswith='T')
    html = ""
    for character in list:
        html= html + character.name+"<br>"
    return HttpResponse(html)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from characters.models import Character
# Create your views here.


def list(request):
    list = Character.objects.all()
    return render(request, 'characters/index.html',{"list":list })


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

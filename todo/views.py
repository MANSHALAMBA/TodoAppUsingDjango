from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todoitem

# Create your views here.
# def mytodoview(request):
#     return HttpResponse("Hello welcome to my todo web app")

def mytodoview(request):
    items=Todoitem.objects.all()
    return render(request,'todo.html' ,
    {'items':items} ,
    )

def addtodo(request):
    newitem=Todoitem(content=request.POST['content'])
    newitem.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request,todoitemid):
    itemtodelete=Todoitem.objects.get(id=todoitemid)
    itemtodelete.delete()
    return HttpResponseRedirect('/todo/')
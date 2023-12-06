from django.shortcuts import render
from todolist.models import Todolist
from todolist.forms import TodolistForm

def index(request):
    context = {}
    form = TodolistForm()
    todolists = Todolist.objects.all()
    context['todolists'] = todolists
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TodolistForm(request.POST)
            else:
                todolist = Todolist.objects.get(id=pk)
                form = TodolistForm(request.POST, instance=todolist)
            form.save()
            form = TodolistForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            todolist = Todolist.objects.get(id=pk)
            todolist.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            todolist = Todolist.objects.get(id=pk)
            form = TodolistForm(instance=todolist)
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)


def ManageAgent(request):
    return render(request, 'Admin/ManageAgent.html')

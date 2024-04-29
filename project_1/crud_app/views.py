from django.shortcuts import render, redirect

from crud_app.forms import LaptopForm
from crud_app.models import Laptop


# Create your views here.


def laptop_create_view(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    template_name = 'crud_app/laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)


def laptop_retrieve_view(request):
    objs = Laptop.objects.all()
    template_name = 'crud_app/laptop_list.html'
    context = {'data': objs}
    return render(request, template_name, context)


def laptop_update_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    form = LaptopForm(instance=obj)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect('retrieve_url')
    template_name = 'crud_app/laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)


def laptop_delete_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('retrieve_url')
    template_name = 'crud_app/delete.html'
    context = {'obj': obj}
    return render(request, template_name, context)



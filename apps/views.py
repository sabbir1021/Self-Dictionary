from django.shortcuts import render, redirect, HttpResponse
from .models import list
from .forms import listFrom
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def home(request):
    if request.method == "POST":
        form = listFrom(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request, ('item has been added to list'))
            return render(request, "home.html", {"all_items": all_items})
    

    all_items = list.objects.all().order_by("-id")
    search = request.GET.get('q')
    if search:
        all_items = all_items.filter(
            Q(english__icontains=search) |
            Q(bangla__icontains=search)
        )
    return render(request, "home.html", {"all_items": all_items})



def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('item has been Deleted'))
    return redirect("home")


def edit(request, list_id):
    if request.method == "POST":
        item = list.objects.get(pk=list_id)
        form = listFrom(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('item has been Edited'))
            return redirect("home")

    else:
        all_items = list.objects.get(pk=list_id)
        return render(request, "edit.html", {"all_items": all_items})

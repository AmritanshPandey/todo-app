from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objectives.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'home.html', {'all_item': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items'})

from django.shortcuts import render, redirect

from .models import *
from .forms import *


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'image_crop/photo_list.html', {'form': form, 'photos': photos})
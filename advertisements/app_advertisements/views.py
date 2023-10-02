from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .models import Advertisement
from .forms import AdvertisementForms


def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements':advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def adv_post(request):
    if request.method=="POST":
        form = AdvertisementForms(request.POST, request.FILES)
        if form.is_valid():
            advertisement=Advertisement(**form.cleaned_data)
            advertisement.user=request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForms()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

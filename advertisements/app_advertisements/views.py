from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy

from .models import Advertisement
from .forms import AdvertisementForm


def index(request):
    title=request.GET.get('query')
    print(title)
    if title:
        advertisements=Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context={'advertisements':advertisements,
             'title': title}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    users=User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context={'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
def adv_post(request):
    if request.method=="POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement=form.save(commit=False)
            new_advertisement.user=request.user
            new_advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def adv_detail(request, pk):
    advertisements = Advertisement.objects.get(id=pk)
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/advertisement.html', context)
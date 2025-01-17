from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers_all = Youtuber.objects.all()
    data = {
        'sliders': sliders,
        'teams': teams,     
        'featured_youtubers': featured_youtubers,
        'youtubers_all': youtubers_all,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')


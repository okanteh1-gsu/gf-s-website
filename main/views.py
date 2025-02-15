from django.shortcuts import render

from main.models import HerInfo, RomanticImage


# Create your views here.

def home(request):
    her_info = HerInfo.objects.all()
        
    return render(request, 'main/home.html',{"her_info": her_info})

def about(request):
    about_img = RomanticImage.objects.first()
    return render(request, 'main/about.html',{"about_img": about_img})
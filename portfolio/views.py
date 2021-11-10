from django.shortcuts import render

from .models import Profile,Skill,Works
# Create your views here.
def index(request):
    #一番最後の１個取得
    profile = Profile.objects.all().last()
    skills = Skill.objects.all()
    works = Works.objects.all()
    #最新のものを３つ
    context = {
        'profile':profile,
        'skills':skills,
        'works':works,
    }
    return render(request, 'index.html', context)

def work(request):
    works = Works.objects.all()
    context = {
        'works':works
    }
    return render(request, 'works.html', context)
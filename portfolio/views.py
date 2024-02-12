from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from portfolio.forms import FeedbackForm
from portfolio.models import Profile, Experience


# Create your views here.

def profile(request):
    pic = Profile.objects.all()
    exp = Experience.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(profile)
    else:
        form = FeedbackForm()

    context = {
        'pic': pic,
        'exp': exp,
        'form': form
    }

    return render(request, 'index.html', context)



import random

from django.shortcuts import render
from .models import *

def home(request):
    flags = Flag.objects.all()
    guessed_country = random.choice(flags)
    countries_to_guess = random.sample(list(flags), 3)
    if guessed_country not in countries_to_guess:
        countries_to_guess[-1] = guessed_country
        random.shuffle(countries_to_guess)

    context = {'flags': flags, 'countries_to_guess': countries_to_guess, 'guessed_country': guessed_country}
    return render(request, 'quiz_app/home.html', context)
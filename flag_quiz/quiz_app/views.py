import random
from django.contrib import messages
from django.shortcuts import render
from .models import *


def home(request):
    # Retrieve the current 'result' value from the session or set it to 0 if it doesn't exist
    result = request.session.get('result', 0)

    countries = Country.objects.all()
    guessed_country = random.choice(countries)

    if str(guessed_country) in request.POST:
        result += 1
        # Store the updated 'result' value in the session
        request.session['result'] = result

    countries_to_guess = random.sample(list(countries), 3)
    if guessed_country not in countries_to_guess:
        countries_to_guess[-1] = guessed_country
        random.shuffle(countries_to_guess)

    context = {'flags': countries, 'countries_to_guess': countries_to_guess,
               'guessed_country': guessed_country, 'result': result}
    return render(request, 'quiz_app/home.html', context)
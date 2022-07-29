import random
import string
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    # characters = list('abcdefghijklmnopqrstuvwxyz')
    characters = list(string.ascii_lowercase)
    numbers = list(string.digits)
    print(numbers)
    special_characters = list('!$#%&/()')

    generated_password = ''

    password_length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list(special_characters))

    if request.GET.get('numbers'):
        characters.extend(list(numbers))

    for _ in range(password_length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})

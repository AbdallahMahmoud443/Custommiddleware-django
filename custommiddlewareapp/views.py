from django.shortcuts import render

# Create your views here.

def index(requets):
    return render(requets,'custommiddlewareapp/index.html')
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def jose(request):

    return render(request, 'jose.html')

def italo(request):

    return render(request, 'italo.html')


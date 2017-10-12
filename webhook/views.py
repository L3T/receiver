from django.shortcuts import render

# Create your views here.

def webhook(request):
    print(request.POST.__dict__)
from django.shortcuts import render

def index(request):
    return render(request,'templates/reactapp/index.html')
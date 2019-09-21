from django.shortcuts import render
from . import views
from .models import Upload

# Create your views here.
def Upload(request):
    return render(request, 'blog/upload.html', {'Upload':Upload})

def up(request):
    return render(request, 'blog/up.html', {'up':up})

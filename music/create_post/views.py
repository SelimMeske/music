from django.shortcuts import render

# Create your views here.
def create_post(request):
    return render(request, '<h1>hi</hi>')

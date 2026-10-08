from django.shortcuts import render

# Create your views here.

def vista(request):
    return render(request, 'home_edgard_jose/home.html')
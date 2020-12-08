from django.shortcuts import render

# Create your views here.
def vchome(request):
    return render(request,'vchome.html')
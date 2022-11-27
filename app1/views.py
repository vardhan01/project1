from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funn(request):
    return HttpResponse('heloo')

def vardan(request):
    d={'a':100,'age':22}
    return render(request,'he.html',d)
def sandesh(request):
    d={'name':'sandesh','age':22}
    return render(request,'he.html',d)
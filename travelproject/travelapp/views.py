from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Actor

#def demo(request):
 #   return HttpResponse("Hello World")
# Create your views here.
def demo1(request):
    obj=Place.objects.all()
    obj2=Actor.objects.all()
    return render(request,"index.html",{"result":obj,
                                        "result2":obj2})

# def alone(request):
#     x=int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res=x+y
#     return render(request,"alone.html",{"result":res})
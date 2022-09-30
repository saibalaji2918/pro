from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def show(request):
    d={'data':5,'a':[1,2,3],'b':'sameera','c':{'ab':'123','bc':'456'},'d':'saibalaji'}
    return render(request,'show.html',d)
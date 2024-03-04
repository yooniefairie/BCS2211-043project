from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mentor.models import Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    
    return render(request,"index.html")

def newmentor(request):
    displaydata=Mentor.objects.all().values()
    if request.method=='POST':
        menid1=request.POST['mentorid']
        menname1=request.POST['mentorname']
        menroomno1=request.POST['mentorroomno']
        data=Mentor(menid=menid1, menname=menname1,menroomno=menroomno1)
        data.save()

        context={
        'displaydata':displaydata,
        'message': 'NEW MENTOR HAS BEEN SAVE'
        }
        
        return render(request,"newmentor.html",context)
    else:
        dict={
            'message': '',
            'displaydata':displaydata,
        }
    return render(request,"newmentor.html",dict)


def searchpage(request):
    findmentor = Mentor.objects.filter(Q(menid=request.GET.get('search')))
    dict={
        'findmentor': findmentor
    }
    return render(request, 'searchpage.html', dict)
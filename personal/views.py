from django.shortcuts import render



APPNAME = 'personal'

# Create your views here.


def renderHomeView(request) :
    context = {}

    # print("in home view")
    return render(request, APPNAME + '/home.html', context)
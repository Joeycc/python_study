from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models
# Create your views here.


def index(request):
    #return HttpResponse('hello world!')
    userlist = []
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        models.UserInfo.objects.create(user=username, pwd=password)

    userlist = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': userlist})
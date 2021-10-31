from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are in the hotel project")


def userList(request):
    User = get_user_model()
    users = User.objects.values()
    return HttpResponse(list(users))

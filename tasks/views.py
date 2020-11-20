from django.shortcuts import render
from django.http import HttpResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task 
from rest_framework import generics


def getList(request):
    return HttpResponse('Hello, welcome to the index page.')

def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be.')

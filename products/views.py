from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('hello!')


def new_product(request):
    return HttpResponse('new!!!!!!!!!')

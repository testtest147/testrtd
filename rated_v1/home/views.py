from django.shortcuts import render
from django.http import HttpReponse

def index(request):
	return HttpReponse('Hello world')

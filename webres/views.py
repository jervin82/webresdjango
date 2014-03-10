from django.shortcuts import render

def webresume(request):
	return render(request, 'base.html',)

def hello(request):
	return render(request, 'page2.html',)

def aboutme(request):
	return render(request, 'page3.html',)

def projects(request):
	return render(request, 'page4.html',)
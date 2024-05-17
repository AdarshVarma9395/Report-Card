from django.shortcuts import render

def homePage(request):
    context = {}
    return render(request, 'myapp/homepage.html', context)

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

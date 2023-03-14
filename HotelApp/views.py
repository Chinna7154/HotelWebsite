from django.shortcuts import render

def index(request):
    return render(request, 'HotelApp/index.html')

def about(request):
    return render(request, 'HotelApp/about.html')

def contact(request):
    return render(request, 'HotelApp/contact.html')

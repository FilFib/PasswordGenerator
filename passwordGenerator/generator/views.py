from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def password(request):
    length = request.POST.get('length')
    big = request.POST.get('big')
    numbers = request.POST.get('numbers')
    specials = request.POST.get('specials')
    return render(request, 'password.html', {'length':length})

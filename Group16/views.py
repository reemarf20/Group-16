from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = ''

    context = {
        'user': user,
        'hello': hello,
        'image_path': 'media_root/picsquad.jpg',
    }
    return render(request, 'main/home.html', context)
    #return HttpResponse("Hello World")
from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(request, chat_name):
    return render(request, 'chat/room.html', {'chat_name': chat_name})

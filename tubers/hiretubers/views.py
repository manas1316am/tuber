from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages

# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        state = request.POST['state']
        user_id = request.POST['user_id']

        # TODO: do all sanitization
        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              city=city, phone=phone, email=email, message=message, state=state, user_id=user_id)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
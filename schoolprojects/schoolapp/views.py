from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from schoolapp.models import form

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):

    return render(request,'index.html',)


def forms(request):
        if request.method == 'post':
            first_name = request.post.get('first_name')
            last_name = request.post.get('last_name')
            grnder=request.post.get('gender')
            dateofbirth = request.post.get('dateofbirth')
            phone_number = request.post.get('phone_number')
            email = request.post.get('email')
            department = request.post.get('department')
            course = request.post.get('course')
            purpose = request.post.get('purpose')

            Form = form(first_name=first_name, last_name=last_name,grnder=grnder, dateofbirth=dateofbirth, phone_number=phone_number,
                        email=email, department=department, course=course, purpose=purpose)
            Form.save()
            print("order confirmed")
        return render(request, 'form.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

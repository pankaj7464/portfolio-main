from django.shortcuts import render
from django.conf.urls.static import static
from .models import contact
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        content = {'name': name, 'email': email,
                   'subject': subject, 'message': message}

        message = '''
From :{}

Subject : {}


New Message :
{}
<a href = ""> hello</a>
Name : {}
        '''.format(content['email'], content['subject'], content['message'], content['name'])
        send_mail(content['subject'], message, '',
                  ['devilsdevelopers9@gmail.com'])
        messages.success(request, 'Congratulation ! Your has been Submitted')
    return render(request, 'index.html')

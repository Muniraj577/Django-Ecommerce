from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins


# Create your views here.

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            try:
                send_mail(subject, message, email, ['munirajrajbanshi5@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        # return redirect('success')
    return render(request, 'contact/contact.html', {'form': form})


# def success(request):
#     return HttpResponse('Success! Thank you for your message.')


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             subject = 'You have a new Contact from {}:{}'.format(email)
#             message = 'Subject: {}\n\nMessages: {}'.format(form.cleaned_data['subject'], form.cleaned_data['message'])
#             mail_admins(subject, message)
#             form.save()
#             messages.add_message(request, messages.INFO, 'Contact submitted.')
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})

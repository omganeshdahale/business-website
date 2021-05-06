from secrets import token_urlsafe
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myproject.settings import EMAIL_HOST_USER
from .models import Subscriber
from .forms import SubscriberForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                sub = Subscriber.objects.get(email=cd.get('email'))
            except ObjectDoesNotExist as e:
                sub = Subscriber(
                    email=cd.get('email'),
                    conf_token=token_urlsafe()
                )

            sub.save()

            conf_link = f'{request.build_absolute_uri("/confirm/")}'
            conf_link += f'?email={sub.email}&conf_token={sub.conf_token}'

            # send confirmation email
            subject = 'Confirmation Email'
            html = render_to_string(
                'email/newsletter_confirm.html', {'conf_link': conf_link})
            plain = strip_tags(html)
            from_ = EMAIL_HOST_USER
            to = sub.email

            send_mail(subject, plain, from_,
                [to], html_message=html)


            msg = 'Thank you for signing up for our email newsletter!'
            msg += ' please see the email we sent you to confirm its you.'
            messages.success(request, msg)

    return redirect('home')

def confirm(request):
    try:
        sub = Subscriber.objects.get(email=request.GET.get('email'))
        if (not sub.confirmed and 
                sub.conf_token == request.GET.get('conf_token')):
            sub.confirmed = True
            sub.conf_token = token_urlsafe()
            sub.save()
            messages.success(request, 'Your email has been confirmed!')

        else:
            messages.error(
                request,
                'Email already confirmed or link is invalid.'
            )

    except ObjectDoesNotExist as e:
        messages.error(request, 'Confirmation link is invalid!')

    return redirect('home')

def unsubscribe(request):
    try:
        sub = Subscriber.objects.get(email=request.GET.get('email'))
        if sub.confirmed and sub.conf_token == request.GET.get('conf_token'):

            sub.delete()
            messages.success(request, 'You are now unsubscribed!')

        else:
            messages.error(request, 'Unsubscription link is invalid!')

    except ObjectDoesNotExist as e:
        messages.error(request, 'Unsubscription link is invalid!')

    return redirect('home')

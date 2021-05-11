from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myproject.settings import EMAIL_HOST_USER
from .forms import ChoiceForm, CONTACT_FORMS
from newsletter.forms import SubscriberForm

def home(request):

    co_forms = {}
    for form_string in CONTACT_FORMS:
        co_forms[form_string] = CONTACT_FORMS[form_string]()

    context = {
        'ch_form': ChoiceForm(),
        'co_forms': co_forms,
        'news_form': SubscriberForm(),
    }

    return render(request, 'core/home.html', context)

def contact(request, form_string):
    if request.method == 'POST':
        try:
            form = CONTACT_FORMS[form_string](request.POST)
            if form.is_valid():
                form.save()

                msg = 'Thank you for connecting with '
                msg += 'us we will reach to you soon!'
                messages.success(request, msg)


                cd = form.cleaned_data
                try:
                    name_in_email = form.name_in_email 
                except AttributeError:
                    name_in_email = 'Contact'

                # send thanks email to user
                if 'email' in cd:
                    subject = 'Thank You!'
                    html = render_to_string('email/contact_thanks.html')
                    plain = strip_tags(html)
                    from_ = EMAIL_HOST_USER
                    to = [cd.get('email')]

                    send_mail(subject, plain, from_,
                        to, html_message=html)

                # send notification email to admins
                subject = f'New {name_in_email}'
                html = render_to_string(
                    'email/contact_notify.html',
                    {'cd': cd}
                )
                plain = strip_tags(html)
                from_ = EMAIL_HOST_USER
                to = [user.email 
                    for user in User.objects.filter(is_superuser=True)]

                send_mail(subject, plain, from_,
                    to, html_message=html)

            else:
                messages.error(request, 'Form is invalid.')

        except KeyError:
            messages.error(request, 'Invalid URL')

    return redirect('home')

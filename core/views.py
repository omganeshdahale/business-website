from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myproject.settings import EMAIL_HOST_USER
from .forms import ChoiceForm, CONTACT_FORMS

def home(request):

    co_forms = {}
    for form_constant in CONTACT_FORMS:
        co_forms[form_constant] = CONTACT_FORMS[form_constant]()

    context = {
        'ch_form': ChoiceForm(),
        'co_forms': co_forms
    }

    return render(request, 'core/home.html', context)

def contact(request, form_constant):
    if request.method == 'POST':
        try:
            form = CONTACT_FORMS[form_constant](request.POST)
            if form.is_valid():
                form.save()

                msg = 'Thank you for connecting with '
                msg += 'us we will reach to you soon!'
                messages.success(request, msg)


                cd = form.cleaned_data
                try:
                    NAME_IN_EMAIL = form.NAME_IN_EMAIL 
                except AttributeError:
                    NAME_IN_EMAIL = 'Contact'

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
                subject = f'New {NAME_IN_EMAIL}'
                html = render_to_string(
                    'email/contact_notify.html',
                    {'NAME_IN_EMAIL': NAME_IN_EMAIL, 'cd': cd}
                )
                plain = strip_tags(html)
                from_ = EMAIL_HOST_USER
                to = [user.email 
                    for user in User.objects.filter(is_superuser=True)]

                send_mail(subject, plain, from_,
                    to, html_message=html)

        except KeyError:
            messages.error(request, 'Invalid URL')

    return redirect('home')

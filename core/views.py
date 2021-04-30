from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myproject.settings import EMAIL_HOST_USER
from .forms import (
    ChoiceForm,
    GeneralForm,
    JoinForm,
    JobForm)

CONTACT_FORMS = {
    GeneralForm.CONSTANT: GeneralForm,
    JoinForm.CONSTANT: JoinForm,
    JobForm.CONSTANT: JobForm,
}

def home(request):
    if request.method == 'POST':
        ch_form = ChoiceForm(request.POST)

        if ch_form.is_valid():
            cd = ch_form.cleaned_data
            # get and instantiate form
            co_form = CONTACT_FORMS[cd.get('form_name')]()

        else:
            ch_form = ChoiceForm()
            co_form = CONTACT_FORMS[ChoiceForm.DEFAULT]

            msg = 'No form available for given subject!'
            messages.error(request, msg)

    else:
        ch_form = ChoiceForm()
        co_form = CONTACT_FORMS[ChoiceForm.DEFAULT]

    context = {
        'ch_form': ch_form,
        'co_form': co_form,
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

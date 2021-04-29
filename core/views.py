from django.shortcuts import render, redirect
from django.contrib import messages
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

        except KeyError as e:
            messages.error(request, 'Invalid URL')

    return redirect('home')

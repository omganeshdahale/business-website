from django.shortcuts import render
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

    context = {
        'ch_form': ch_form,
        'co_form': co_form
    }
    return render(request, 'core/home.html', context)

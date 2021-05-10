from django.forms import (
    ChoiceField,
    TextInput,
    Textarea,
    Select,
    Form,
    ModelForm)
from .models import (
    GeneralContact,
    JoinContact,
    JobContact)

# Define form strings (urlsafe)
GENERAL_FORM = 'GF'
JOIN_FORM = 'JnF'
JOB_FORM = 'JbF'

phone_attrs = {
    'type': 'tel',
    'pattern': r'^\d{4,15}$',
    'title': 'Only digits are allowed and length must be between 4 to 15.',
}

class ChoiceForm(Form):
    '''Form to choose type of form'''

    FORM_CHOICES = (
        (GENERAL_FORM, 'General Inquiry'),
        (JOIN_FORM, 'Join The Gym'),
        (JOB_FORM, 'Apply For Job'),
    )

    form_name = ChoiceField(
        label='Subject',
        initial=GENERAL_FORM,
        choices=FORM_CHOICES,
        widget=Select(attrs={'id':'ch_form-select'}),
    )


class GeneralForm(ModelForm):
    name_in_email = 'General Inquiry'

    class Meta:
        model = GeneralContact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(attrs={'rows': 5})
        }


class JoinForm(ModelForm):
    name_in_email = 'Join Inquiry'

    class Meta:
        model = JoinContact
        fields = ['name', 'email', 'dial_code', 'phone']
        widgets = {
            'phone': TextInput(attrs=phone_attrs)
        }


class JobForm(ModelForm):
    name_in_email = 'Job Inquiry'

    class Meta:
        model = JobContact
        fields = ['name', 'email', 'dial_code', 'phone']
        widgets = {
            'phone': TextInput(attrs=phone_attrs)
        }


# Map form strings
CONTACT_FORMS = {
    GENERAL_FORM: GeneralForm,
    JOIN_FORM: JoinForm,
    JOB_FORM: JobForm,
}

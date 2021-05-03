from django.forms import ChoiceField, Textarea, Select, Form, ModelForm
from .models import (
    GeneralContact,
    JoinContact,
    JobContact)

# Define form constants
GENERAL_FORM = 'GF'
JOIN_FORM = 'JiF'
JOB_FORM = 'JbF'

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
    NAME_IN_EMAIL = 'General Inquiry'

    class Meta:
        model = GeneralContact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(attrs={'rows': 5})
        }


class JoinForm(ModelForm):
    NAME_IN_EMAIL = 'Join Inquiry'

    class Meta:
        model = JoinContact
        fields = ['name', 'email', 'phone']


class JobForm(ModelForm):
    NAME_IN_EMAIL = 'Job Inquiry'

    class Meta:
        model = JobContact
        fields = ['name', 'email', 'phone']


# Map form constants
CONTACT_FORMS = {
    GENERAL_FORM: GeneralForm,
    JOIN_FORM: JoinForm,
    JOB_FORM: JobForm,
}

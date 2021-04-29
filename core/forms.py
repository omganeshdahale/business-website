from django.forms import ChoiceField, Select, Form, ModelForm
from .models import (
    GeneralContact,
    JoinContact,
    JobContact)

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
    DEFAULT = GENERAL_FORM

    form_name = ChoiceField(
        label='Subject',
        initial=DEFAULT,
        choices=FORM_CHOICES,
        widget=Select(attrs={'id':'ch_form-select'}),
    )


class GeneralForm(ModelForm):
    CONSTANT = GENERAL_FORM

    class Meta:
        model = GeneralContact
        fields = ['name', 'email', 'message']


class JoinForm(ModelForm):
    CONSTANT = JOIN_FORM

    class Meta:
        model = JoinContact
        fields = ['name', 'email', 'phone']


class JobForm(ModelForm):
    CONSTANT = JOB_FORM

    class Meta:
        model = JobContact
        fields = ['name', 'email', 'phone']

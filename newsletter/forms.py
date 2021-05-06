from django.forms import EmailField, Form

class SubscriberForm(Form):
    email = EmailField(max_length=100)

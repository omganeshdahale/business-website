from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

INDIA = '+91'
US = '+1'
GERMANY = '+49'
JAPAN = '+81'
FRANCE = '+33'
SWITZERLAND = '+41'

DIALCODE_CHOICES = (
    (INDIA, INDIA + ' (India)'),
    (US, US + ' (US)'),
    (GERMANY, GERMANY + ' (Germany)'),
    (JAPAN, JAPAN + ' (Japan)'),
    (FRANCE, FRANCE + ' (France)'),
    (SWITZERLAND, SWITZERLAND + ' (Switzerland)'),
)

class Contact(models.Model):
    '''Abstract class for Contacts'''

    date_created = models.DateField(verbose_name="Created on date",
        auto_now_add="True")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.date_created:%b %-d, %Y} : {self.name}'

    class Meta:
        abstract = True


class Phone(models.Model):
    dial_code = models.CharField(
        max_length=4,
        choices=DIALCODE_CHOICES,
        default=INDIA,
    )
    phone = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(4),
            RegexValidator(
                regex=r'^\d*$',
                message='Only digits are allowed.'
            )
        ]
    )

    def __str__(self):
        return f'{self.dial_code} {self.phone}'

    class Meta:
        abstract = True


class GeneralContact(Contact):
    message = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'General Inquiry'
        verbose_name_plural = 'General Inquiries'


class JoinContact(Contact, Phone):

    class Meta:
        verbose_name = 'Join Gym Inquiry'
        verbose_name_plural = 'Join Inquiries'


class JobContact(Contact, Phone):

    class Meta:
        verbose_name = 'Job Inquiry'
        verbose_name_plural = 'Job Inquiries'

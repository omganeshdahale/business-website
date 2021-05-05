from django.db import models

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


class GeneralContact(Contact):
    message = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'General Inquiry'
        verbose_name_plural = 'General Inquiries'


class JoinContact(Contact):
    phone = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Join Gym Inquiry'
        verbose_name_plural = 'Join Inquiries'


class JobContact(Contact):
    phone = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Job Inquiry'
        verbose_name_plural = 'Job Inquiries'

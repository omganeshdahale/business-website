from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    conf_token = models.CharField(max_length=43)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email} ({"" if self.confirmed else "not"} confirmed)'


class Newsletter(models.Model):
    date_created = models.DateField(verbose_name="Created on date",
        auto_now_add="True")
    subject = models.CharField(max_length=100)
    body = models.TextField()
    broadcast = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.subject}'
            + f' ({"" if self.broadcast else "not"} broadcasted)')

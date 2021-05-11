from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myproject.settings import EMAIL_HOST_USER
from .models import Subscriber, Newsletter

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        for sub in Subscriber.objects.filter(confirmed=True):
            url = f'{request.build_absolute_uri("/unsubscribe/")}'
            url += f'?email={sub.email}&conf_token={sub.conf_token}'

            subject = newsletter.subject
            html = newsletter.body
            html += ('<hr style="margin-top: 1rem;margin-bottom: 1rem;'
                'border: 0;border-top: 1px solid rgba(0,0,0,.1);">'
                '<small style="font-size: 12px;color: #555555">'
                'don\'t want to recieve emails? you can '
                f'<a href={url}>unsubscribe here.</a></small>')
            plain = strip_tags(html)
            from_ = EMAIL_HOST_USER
            to = sub.email

            send_mail(subject, plain, from_,
                [to], html_message=html)

        newsletter.broadcast = True
        newsletter.save()

send_newsletter.short_description = "Broadcast"

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'broadcast', 'date_created')
    actions = [send_newsletter]
    exclude = ('broadcast',)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirmed')
    exclude = ('conf_token', 'confirmed')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

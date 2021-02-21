from django.contrib import admin

from .models import Mail, Recipient

admin.site.register(Mail)
admin.site.register(Recipient)
from django.contrib import admin
from .models import Member, Event, Payment

admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Payment)

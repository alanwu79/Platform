from django.contrib import admin

# Register your models here.
from app.models import Topic
from app.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)
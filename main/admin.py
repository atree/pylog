from django.contrib import admin
from main.models import *

admin.site.register(Device, DeviceAdmin)
admin.site.register(Entry, EntryAdmin)

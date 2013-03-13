from django.db import models
from django.contrib import admin

class Device(models.Model):
    _id = models.CharField(max_length = 200, null = True, blank = True)
    last_updated = models.DateTimeField()

    def __unicode__(self):
        return "%s" % self._id

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('_id', 'last_updated')

class Entry(models.Model):
    device = models.ForeignKey(Device)
    cr_date = models.DateTimeField()
    value = models.TextField(null = True, blank = True)

    def __unicode__(self):
        return "%s - %s" % (self.device, self.value)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('device', 'cr_date')



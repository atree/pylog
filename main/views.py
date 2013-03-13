from django.http import HttpResponse
from main.models import *
import datetime

def log_entry(request):

    if request.GET.get('id'):
        the_id = request.GET.get('id')
        the_msg = request.GET.get('msg')
    if request.POST.get('id'):
        the_id = request.POST.get('id')
        the_msg = request.POST.get('msg')

    rightnow = datetime.datetime.now()

    d = Device.objects.filter(_id = the_id)
    if len(d) == 0:
        print "creating a new device: %s" % (d) 
        d = Device(_id = the_id, last_updated = rightnow)
        d.save()
    else:
        d = d[0]
    e = Entry(device = d, cr_date = rightnow, value = the_msg)
    e.save()
    print "creating a new entry: %s" % (e)

    return HttpResponse(status=200)


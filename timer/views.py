from django.shortcuts import render
from .models import Event
import datetime
from datetime import date

# Create your views here.

def event_list(request):
    events=Event.objects.order_by('time')
    for event in events:
        event.time_until_event=(event.time-datetime.date.today()).days
    return render(request, 'timer/event_list.html',{'events':events})

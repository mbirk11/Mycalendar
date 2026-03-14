from django.shortcuts import render
from .models import Event
from datetime import date
import calendar

def index(request):
    # Retrieve the first event to display its date, or fallback to today.
    event = Event.objects.first()
    
    if event:
        d = event.start_time
    else:
        d = date.today()
        
    # Get standard calendar matrix for the month
    cal = calendar.HTMLCalendar(calendar.MONDAY)
    month_days = cal.monthdayscalendar(d.year, d.month)
    month_name = calendar.month_name[d.month]
        
    context = {
        'year': d.year,
        'month': d.month,
        'day': d.day,
        'month_name': month_name,
        'month_days': month_days,
    }
        
    return render(request, 'calendar_app/index.html', context)






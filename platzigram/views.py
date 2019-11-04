from django.http import HttpResponse
from datetime import datetime
# Para devolver json
import json
def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def sort_integers(request):
    # numbers = list(map(int,request.GET['numbers'].split(',')))
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sNumbers = sorted(numbers)
    
    data = {
        'status':'ok',
        'numbers': sNumbers,
        'message': 'Integers sorted sucessfully'
    }
    return HttpResponse(
        json.dumps(data,indent=4),
        content_type='application/json')
def say_hi(request,name,age):
    if age < 12:
        message = 'Sorry {} youre not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to Platzigram!'.format(name)
    return HttpResponse(message)
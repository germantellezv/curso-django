from django.http import HttpResponse
from datetime import datetime
# Para devolver json
import json
def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
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
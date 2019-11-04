""" Posts views """
# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
posts = [
    {
        'name':'Montblanc',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?image=1036',
    },
    {
        'name':'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?image=903',
    },
    {
        'name':'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?image=1076',
    }

]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i> {timestamp}</i></small></p>
            <figure><img src="{picture}">/</figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
""" Posts views """
# from django.shortcuts import render
from django.shortcuts import render


# Utilities
from datetime import datetime
posts = [
    {
        'title':'Montblanc',
        'user': {
            'name':'Yésica Cortés',
            'picture': 'http://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/400/400/?image=1036',
    },
    {
        'title':'Via Láctea',
        'user': {
            'name':'Christian Van der Henst',
            'picture': 'http://picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/400/400/?image=903',
    },
    {
        'title':'Nuevo auditorio',
        'user': {
            'name':'Uriel (thespianartist)',
            'picture': 'http://picsum.photos/60/60/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/400/400/?image=1076',
    },

]

def list_posts(request):
    return render(request,'posts/feed.html',{'posts':posts})
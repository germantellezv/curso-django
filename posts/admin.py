#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','title','user','photo','modified','created')
    list_display_links = ('pk','title')
    list_filter = ('created',)

    # Opciones por implementar
    """ list_display_links = ('pk','user')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website','picture')

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
        )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff')
    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra Info',{
            'fields':(('website','phone_number'),('biography'))
        }),
        ('Metadata',{
            'fields': (('created','modified'),),
        })
    )
    readonly_fields = ('created','modified') """
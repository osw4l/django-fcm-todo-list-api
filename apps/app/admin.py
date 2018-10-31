from django.contrib import admin
from . import models
# Register your models here.


admin.site.site_header = 'osw4l started kit Admin'
admin.site.site_title = 'osw4l started kit Admin'
admin.site.index_title = 'osw4l started kit Admin'


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'description',
        'ready'
    ]


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'body',
        'created',
        'send'
    ]
    actions = ['send_again']

    def send_again(self, request, queryset):
        for obj in queryset:
            obj.increment_send()
            obj.send_push_notification()

    send_again.short_description = 'send notification/s again'

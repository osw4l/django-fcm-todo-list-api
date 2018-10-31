from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.fcm.models import Device
from . import constants


# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey('auth.User', blank=True)
    description = models.CharField(max_length=50)
    ready = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Todos'
        verbose_name_plural = 'Todos'

    def set_status(self):
        self.ready = not self.ready
        self.save()
        self.send_push_notification()

    def send_push_notification(self):
        for device in Device.objects.filter(user=self.user):
            device.send_message(self.get_notification_data())

    def get_notification_data(self):
        return {"notification": {
            "title": "task {} ready".format(self.id),
            "body": "your task with id {} was marked as ready".format(
                self.id
            )
        }}


class Notification(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    send = models.PositiveIntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.send_push_notification()
            self.send += 1
        super().save(*args, **kwargs)

    def increment_send(self):
        self.send += 1
        self.save(update_fields=['send'])

    def send_push_notification(self):
        for device in Device.objects.filter(is_active=True):
            device.send_message(self.get_notification_data())

    def get_notification_data(self):
        return {"notification": {
            "title": self.title,
            "body": self.body
        }}

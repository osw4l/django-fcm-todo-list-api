from . import models


DEVICE_MODEL = models.Device
API_URL = "https://fcm.googleapis.com/fcm/send"
API_KEY = "AIzaSyD1S1QNoIb5KKzgVh1KTG1DzuK5qNzm96s"
MAX_RECIPIENTS = 1000


def get_device_model():
    return DEVICE_MODEL

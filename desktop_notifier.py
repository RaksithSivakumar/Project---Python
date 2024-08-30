import time
from plyer import notification

def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10
    )
while True:
    notify_me("Reminder","It's time to take a break")
    time.sleep(4000)
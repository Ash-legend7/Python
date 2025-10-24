#drink water reminder
from plyer import notification
import time
m="Please drink water now."
interval=5 #seconds
while True:
    notification.notify(
    title = "Drinking Water Reminder",
    message = m,
    timeout = 1
    )
    import pyttsx3
    engine=pyttsx3.init()
    engine.say(m)
    engine.runAndWait()
    time.sleep(interval)

#in windows,use task scheduler

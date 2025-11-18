from datetime import datetime
from playsound import playsound

alarm = input("Enter alarm time (HH:MM:SSAM / HH:MM:SSPM): ")

# Split by colon
time_part, period = alarm[:-2], alarm[-2:]   # last 2 = AM or PM
alarm_hours, alarm_minutes, alarm_seconds = time_part.split(":")
alarm_period = period.upper()

while True:
    now = datetime.now()
    current_hours = now.strftime("%I")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hours == current_hours:
            if alarm_minutes == current_minutes:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound("digital-watch-alarm.mp3")
                    break

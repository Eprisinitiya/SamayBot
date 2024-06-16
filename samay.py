from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{minutes_left}:{seconds_left}")

    playsound("Samay-alarm.mp3")
minutes = int(input("Enter minutes to wait: "))
seconds = int(input("Enter seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
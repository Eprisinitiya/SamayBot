import time
import random
import os
from playsound import playsound
from gtts import gTTS
import threading
import sys

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

timer_history = []
last_timer = None

#This function announces the left time
def voice_announcement(minutes_left, seconds_left):
    text = f"{minutes_left} minutes and {seconds_left} seconds left."
    tts = gTTS(text)
    tts.save("time_left.mp3")
    playsound("time_left.mp3")
    os.remove("time_left.mp3")

def show_quote():
    quotes = [
        "Keep going, you're doing great!",
        "Stay focused, you're almost there!",
        "Believe in yourself!",
        "Time flies, stay on track!",
        "Consistency is key to success!"
    ]
    print(f"\n💡 {random.choice(quotes)}\n")

#This shows progress
def show_progress_bar(progress, total):
    bar_length = 40
    block = int(round(bar_length * progress / total))
    text = f"[{'#' * block + '-' * (bar_length - block)}] {progress}/{total} seconds"
    sys.stdout.write(f"{CLEAR_AND_RETURN}{text}\n")
    sys.stdout.flush()

#For saving timer history
def save_timer_history(minutes, seconds):
    global last_timer
    timer_history.append((minutes, seconds))
    last_timer = (minutes, seconds)

#Main timer function
def samay(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        #Display progress
        show_progress_bar(time_elapsed, seconds)

        #Announces time at every minute
        if time_left % 60 == 0 and time_left > 0:
            threading.Thread(target=voice_announcement, args=(minutes_left, seconds_left)).start()

        #Show motivational quote at random intervals
        if time_left % 30 == 0 and time_left > 0:
            show_quote()

    #Plays alarm sound
    print("\n⏰ Time's up! \nThanks for using SamayBot🙏")
    playsound("samay-alarm.mp3")  # Ensure this file exists

#Loads the last saved timer if available
if last_timer:
    use_last_timer = input(f"Do you want to use the last saved timer of {last_timer[0]} minutes and {last_timer[1]} seconds? (y/n): ").lower()
    if use_last_timer == 'y':
        minutes, seconds = last_timer
    else:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
else:
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

total_seconds = minutes * 60 + seconds

save_timer_history(minutes, seconds)

#Start the timer
samay(total_seconds)

#This shows timer history
print("\n⏳ Timer History:")
for i, (min_left, sec_left) in enumerate(timer_history, 1):
    print(f"{i}. {min_left} minutes and {sec_left} seconds")

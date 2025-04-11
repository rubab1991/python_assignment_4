import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # \r returns to start of line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
seconds= input('Enter the time in seconds:')
# Example: Countdown from 1 minute (60 seconds)
countdown(int(seconds))

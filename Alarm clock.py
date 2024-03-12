#Project --- Alarm Clock

import time

alarm_time = input("Enter the time for the alarm (hh:mm:ss): ")

try:
    alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
    while True:
        current_time = time.localtime()
        if (current_time.tm_hour, current_time.tm_min, current_time.tm_sec) == (alarm_hour, alarm_minute, alarm_second):
            print("Time's up! Wake up!")  
            break
except ValueError:
    print("Invalid time format. Please use hh:mm:ss format.")

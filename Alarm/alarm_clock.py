import tkinter as tk
from tkinter import ttk
import time
import threading
from playsound import playsound


def set_alarm():
    alarm_time = entry_time.get()
    am_pm = combobox_am_pm.get()

    try:
        alarm_time = time.strptime(f"{alarm_time} {am_pm}", "%I:%M %p")
        current_time = time.localtime()

        alarm_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                       alarm_time.tm_hour, alarm_time.tm_min, 0, current_time.tm_wday,
                                       current_time.tm_yday, current_time.tm_isdst))

        time_diff = time.mktime(alarm_time) - time.mktime(current_time)

        if time_diff < 0:
            time_diff += 86400  # Add 24 hours to set alarm for the next day

        threading.Timer(time_diff, ring_alarm).start()

        status_label.config(text="Alarm set!")
    except ValueError:
        status_label.config(text="Invalid time format! Use HH:MM AM/PM")


def ring_alarm():
    status_label.config(text="Time to wake up!")
    # Replace "alarm_tone.mp3" with the path to your sound file
    playsound("alarm_tone.mp3")
    # Add any additional actions here, like displaying a popup or stopping the alarm after some time


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create GUI components
label_time = tk.Label(root, text="Enter alarm time:")
label_time.pack(pady=10)

entry_time = tk.Entry(root)
entry_time.pack(pady=5)

# Create the AM/PM selection dropdown
am_pm_values = ["AM", "PM"]
combobox_am_pm = ttk.Combobox(root, values=am_pm_values, state="readonly")
combobox_am_pm.set("AM")
combobox_am_pm.pack(pady=5)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()

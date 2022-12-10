import tkinter as tk
import datetime
import pytz

timezones = ["US/Alaska", "US/Aleutian", "US/Arizona", "US/Central", "US/East-Indiana", "US/Eastern", "US/Hawaii", "US/Indiana-Starke", "US/Michigan", "US/Mountain", "US/Pacific", "US/Samoa"]

def get_timezone_time(e, args):
    select_timezone_listbox = args[0]
    time_label = args[1]
    selection_index = select_timezone_listbox.curselection()
    selected_timezone = select_timezone_listbox.get(selection_index)
    
    now_time = datetime.datetime.now()
    tz_time = now_time.astimezone(pytz.timezone(selected_timezone))
    tz_formatted = tz_time.strftime("%H:%M:%S")

    time_label.configure({"text": f"The time in {selected_timezone} is {tz_formatted}."})
    time_label.update()

root = tk.Tk()
root.title("Nathan's Timezone Application")
window_width = 400
window_height = 175
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((screen_width - window_width)/2)
center_y = int((screen_height - window_height)/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Instance of Label widget class for selection prompt.
select_timezone_label = tk.Label(root, text="Please select a timezone.")

# Instance of Listbox class for selection of timezone from list.
list_var = tk.Variable(value=timezones)
select_timezone_listbox = tk.Listbox(root, listvariable=list_var, height=1)

# Instance of Button class to get the local time in the selected timezone.
select_timezone_button = tk.Button(root, text="Get Time")

# Second instance of the Label class to display the local time in the selected timezone.
time_label = tk.Label(root, text="")

# Place widgets on grid.
select_timezone_label.grid(column=0, row=0, columnspan=4, sticky=tk.W, padx=10, pady=10)
select_timezone_listbox.grid(column=0, row=1, columnspan=3, sticky=tk.EW, padx=10, pady=10)
select_timezone_button.grid(column=4, row=1, sticky=tk.E, padx=10, pady=10)
time_label.grid(column=0, row=4, columnspan=4, sticky=tk.W, padx=10, pady=10)

# Bind button to callback.
select_timezone_button.bind("<Button>", lambda e, args=[select_timezone_listbox, time_label]: get_timezone_time(e, args))

root.mainloop()
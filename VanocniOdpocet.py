import tkinter as tk
import datetime

# Calculate the number of days until the next Christmas
today = datetime.datetime.now()
next_christmas = datetime.datetime(today.year + 1 if today.month == 12 and today.day > 24 else today.year, 12, 24)
delta = next_christmas - today
days_left = delta.days

# Create the GUI window
window = tk.Tk()
window.title("Days until Christmas")

# Define a function to close the window
def on_double_click(event):
    window.destroy()

# Disable the window borders and title
window.overrideredirect(True)

# Get the dimensions of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get the dimensions of the window
window_width = 150
window_height = 60

# Calculate the position of the top-left corner of the window
x = screen_width - window_width
y = screen_height - window_height

# Set the window's position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Add a label to display the number of days left
label = tk.Label(text=f"Do Vánoc zbývá {days_left} dní!")
label.pack()

# Bind the function to the <Double-1> event
window.bind("<Double-1>", on_double_click)

# Run the GUI loop
window.mainloop()

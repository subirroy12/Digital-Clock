import tkinter as tk
from time import strftime

def update_time():
    """Updates the time displayed on the digital clock."""
    string_time = strftime('%H:%M:%S %p')  # Get current time in HH:MM:SS AM/PM format
    digital_clock_label.config(text=string_time)
    digital_clock_label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")  # Set window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="black")  # Set background color

# Create a label to display the time
digital_clock_label = tk.Label(
    root,
    font=('calibri', 40, 'bold'),
    background='black',
    foreground='white'
)
digital_clock_label.pack(pady=40)  # Pack the label with some vertical padding

# Start updating the time
update_time()

# Run the Tkinter event loop
root.mainloop()
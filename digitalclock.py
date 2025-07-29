import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

# Dynamically resize font based on window size
def resize_font(event):
    new_size = min(event.width // 10, event.height // 2)
    label.config(font=("Arial", new_size))

# Main window setup
root = tk.Tk()
root.title("Responsive Digital Clock")
root.configure(bg="black")

# Make window resizable
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create and place label
label = tk.Label(root, font=("Arial", 50), bg="black", fg="cyan")
label.grid(row=0, column=0, sticky="nsew")

# Bind the window resizing event
root.bind("<Configure>", resize_font)

# Start the clock
update_time()
root.mainloop()

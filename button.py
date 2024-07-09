import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to handle button click event
def button_click():
    try:
        messagebox.showinfo("Panic Button Clicked", "We will help you!")
        subprocess.run(['python', 'call.py'], check=True)
        subprocess.run(['python', 'sms.py'], check=True)
        subprocess.run(['python', 'location.py'], check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e}\n\nCheck location.log for details."
        messagebox.showerror("Error", error_message)

# Create the main application window
root = tk.Tk()
root.title("Panic Button Example")

# Create a button widget
button = tk.Button(root, text="panic", command=button_click, bg="pink", fg="white", width=15, height=2)
button.pack(pady=120, padx=150)  # Adjust padding as needed

# Run the Tkinter event loop
root.mainloop()

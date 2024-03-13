import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Short Tkinter Example")

# Create a button and bind the click event to on_button_click
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Create a label
label = tk.Label(root, text="Waiting for button click...")
label.pack()

# Start the Tkinter event loop
root.mainloop()

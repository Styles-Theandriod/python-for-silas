# Event/Buildings
import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Building UI Components Example")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

import tkinter as tk
import sys

def on_file_exit():
    window.destroy()

def on_edit_copy():
    text = text_widget.get("sel.first", "sel.last")
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

def on_closing():
    window.destroy()

window = tk.Tk()
window.title("Menu Example")

# Create a main menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=on_file_exit)

# Edit menu with a submenu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=on_edit_copy)

# Text widget to demonstrate copying text
text_widget = tk.Text(window, height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Handle closing on Mac
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter event loop
window.mainloop()

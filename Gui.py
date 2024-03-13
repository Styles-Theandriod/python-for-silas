
import tkinter as tk

from tkinter import simpledialog

window = tk.Tk()
window.title = 'Hacking for youth'

label = tk.Label(window, text='Hacking for youth')
label.pack()


# message widget

message = tk.Message(window,
    text='this is a multiline text. It can span across multiple lines.',
    width=200,
    font=("Helvetica", 12)
) 
message.pack()


Button = tk.Button(window, text="click me", width=10, fg='red', bg='green', border=20)
Button.pack()

# Check boxes/Radio buttons

#  Check boxes/Radio buttons in tkinker
radio_var = tk.StringVar()

def on_radio_click():
    label.config(text=f"Selected option: {radio_var.get()}")

# create a radio button 
radio_button1 = tk.Radiobutton(
    window,
    text="Option 1",
    variable=radio_var,
    value="Option 1",
    command=on_radio_click
)
radio_button1.pack()

radio_button2 = tk.Radiobutton(
    window,
    text="Option 2",
    variable=radio_var,
    value="Option 2",
    command=on_radio_click
)
radio_button2.pack()

# Entry widget

entry = tk.Entry(window, width=300)
entry.pack()

def on_submit():
    entered_text = entry.get()
    label.config(text=f"You entered {entered_text}")

submit_button = tk.Button(window, width=3, height=3, text="Submit", command=on_submit)
submit_button.pack()

# Canvas widget


# # Canvas widget 



def draw_circle():
    # clear all previous ddrawing from canvas
    canvas.delete('all')

    # Draw a line 
    canvas.create_oval(50,50, 150, 150, fill="red", width=2)

def draw_rectangle():
    # clear all previous ddrawing from canvas
    canvas.delete('all')

    # Draw a line 
    canvas.create_rectangle(50,50, 150, 150, fill="red", width=2)

    
def draw_line():
    # clear all previous ddrawing from canvas
    canvas.delete('all')

    # Draw a line 
    canvas.create_line(50,50, 150, 150, fill="red", width=2)


canvas = tk.Canvas(window, width=200, height=200, bg="white")
canvas.pack()

# Create buttons to trigger different drawings
circle_button = tk.Button(window, text="Draw circle", command=draw_circle)
circle_button.pack()

rectangle_button = tk.Button(window, text="Draw rectangle", command=draw_rectangle)
rectangle_button.pack()

line_button = tk.Button(window, text="Draw line", command=draw_line)
line_button.pack()


def get_text():
    text_content = text_widget.get("1.0", "end-1c")
    print(text_content)

text_widget = tk.Text(window, height=10, width=400)

# Insert initial Text options 
text_widget.insert("1.0", "Hello, this is a Text widget")
text_widget.pack(pady=10)


# create a button to get the text 
get_text_button = tk.Button(window, text="Get Text", command=get_text)
get_text_button.pack()

# Dialog boxes
def show_message_box():
    result = simpledialog.showinfo("Information", "This is an information message!")

def get_user_input():
    user_input = simpledialog.askstring("Input", "Enter something:")
    if user_input:
        print(f"You entered: {user_input}")

def get_user_choice():
    choices = ["Option 1", "Option 2", "Option 3"]
    user_choice = simpledialog.askinteger("Choose", "Select an option (1-3):", minvalue=1, maxvalue=3)
    if user_choice:
        print(f"You chose: {choices[user_choice - 1]}")

def yes_no_question():
    response = simpledialog.askyesno("Question", "Do you want to proceed?")
    if response:
        print("You clicked 'Yes'")
    else:
        print("You clicked 'No'")


message_box_button = tk.Button(window, text="Show Message Box", command=show_message_box)
message_box_button.pack(pady=10)

user_input_button = tk.Button(window, text="Get User Input", command=get_user_input)
user_input_button.pack(pady=10)

user_choice_button = tk.Button(window, text="Get User Choice", command=get_user_choice)
user_choice_button.pack(pady=10)

yes_no_button = tk.Button(window, text="Yes/No Question", command=yes_no_question)
yes_no_button.pack(pady=10)


# Example using Pack Manager
# label1 = tk.Label(window, text="Label 1")
# label1.pack(side="top")

# label2 = tk.Label(window, text="Label 2")
# label2.pack(side="left", fill="both")


# Example using Grid Manager
# label1 = tk.Label(window, text="Label 1")
# label1.grid(row=0, column=0)

# label2 = tk.Label(window, text="Label 2")
# label2.grid(row=0, column=1)

# # Example using Place Manager
# label1 = tk.Label(window, text="Label 1")
# label1.place(x=50, y=20)

# label2 = tk.Label(window, text="Label 2")
# label2.place(relx=0.5, rely=0.5, anchor="center")


# creating a dialog boxes 
from tkinter import messagebox

def show_info_dialog():
    messagebox.showinfo("Information", "This is an information message!")

def show_warning_dialog():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error_dialog():
    messagebox.showerror("Error", "This is an error message!")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to proceed?")
    if result == "yes":
        print("User clicked 'Yes'")
    else:
        print("User clicked 'No'")



# Create buttons to trigger different dialog boxes
info_button = tk.Button(window, text="Show Info", command=show_info_dialog)
info_button.pack(pady=10)

warning_button = tk.Button(window, text="Show Warning", command=show_warning_dialog)
warning_button.pack(pady=10)

error_button = tk.Button(window, text="Show Error", command=show_error_dialog)
error_button.pack(pady=10)

question_button = tk.Button(window, text="Ask Question", command=ask_question)
question_button.pack(pady=10)



def on_button_click():
    label.config(text="Button Clicked!")



# Using pack() geometry manager
# label_pack = tk.Label(window, text="Using pack()")
# label_pack.pack()

# button_pack = tk.Button(window, text="Click Me", command=on_button_click)
# button_pack.pack(pady=10)

# # Using grid() geometry manager
# label_grid = tk.Label(window, text="Using grid()")
# label_grid.grid(row=1, column=1)

# button_grid = tk.Button(window, text="Click Me", command=on_button_click)
# button_grid.grid(row=2, column=1, pady=10)

# # Using place() geometry manager
# label_place = tk.Label(window, text="Using place()")
# label_place.place(x=200, y=50)

# button_place = tk.Button(window, text="Click Me", command=on_button_click)
# button_place.place(x=200, y=100)



def on_file_exit():
    window.destroy()

def on_edit_copy():
    text = text_widget.get("sel.first", "sel.last")
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

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





window.mainloop()
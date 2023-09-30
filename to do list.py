import tkinter as tk

# Function to add a new task
def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        status_label.config(text="Task added.", fg="green")
    else:
        status_label.config(text="Please enter a task.", fg="red")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        status_label.config(text="Task deleted.", fg="green")
    except IndexError:
        status_label.config(text="Please select a task to delete.", fg="red")

# Function to edit the selected task
def edit_task():
    try:
        selected_task_index = task_list.curselection()[0]
        new_task = entry.get()
        if new_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, new_task)
            entry.delete(0, tk.END)
            status_label.config(text="Task edited.", fg="green")
        else:
            status_label.config(text="Please enter a new task.",bg="green", fg="red")
    except IndexError:
        status_label.config(text="Please select a task to edit.", fg="red")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")  # Set the window size

# Customize background and foreground colors
root.configure(bg="lightblue")
entry_bg_color = "white"
entry_fg_color = "black"

# Create a frame for the task list
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

# Create a listbox for the tasks
task_list = tk.Listbox(
    frame, selectbackground="yellow", selectmode=tk.SINGLE, width=40, height=10,
    bg=entry_bg_color, fg=entry_fg_color
)
task_list.pack(side=tk.LEFT)

# Create a scrollbar for the task list
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Connect the scrollbar to the task list
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Create an entry widget for new tasks
entry = tk.Entry(root, width=30, bg=entry_bg_color, fg=entry_fg_color)
entry.pack(pady=10)

# Create buttons for adding, editing, and deleting tasks
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)

add_button.pack()
edit_button.pack()
delete_button.pack()

# Create a label for displaying status messages
status_label = tk.Label(root, text="", fg="green", bg="lightblue")
status_label.pack()

# Run the Tkinter main loop
root.mainloop()
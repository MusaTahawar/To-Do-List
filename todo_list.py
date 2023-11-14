import tkinter as tk

# Function to add a task

def add_task():
    task = task_entry.get()
    
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to mark a task as complete

def complete_task():
    selected_task = task_listbox.curselection()
    
    if selected_task:
        task_listbox.itemconfig(selected_task, {'bg': 'light green'})
        task_listbox.selection_clear(0, tk.END)

# Function to delete a task

def delete_task():
    selected_task = task_listbox.curselection()
    
    if selected_task:
        task_listbox.delete(selected_task)

# Create the main window

root = tk.Tk()
root.title("To-Do List App")

# Create GUI elements

task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
complete_button = tk.Button(root, text="Mark as Complete", command=complete_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)

# Arrange GUI elements on the window

task_entry.pack(pady=10)
add_button.pack(padx = 10, pady = 10)
complete_button.pack(padx = 10, pady = 10)
delete_button.pack(padx = 10, pady = 10)
task_listbox.pack()

root.mainloop()

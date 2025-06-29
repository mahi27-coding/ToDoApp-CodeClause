import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to delete a task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        del tasks[selected[0]]

# Function to mark task as completed
def mark_completed():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, f"✔️ {task}")
        del tasks[selected[0]]
        tasks.append(f"✔️ {task}")

# Input box for tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Mark Completed", command=mark_completed).pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Run the app
root.mainloop()

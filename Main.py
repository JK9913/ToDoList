import tkinter as tk;
from tkinter import messagebox, simpledialog;

class ToDoApp:
    def __init__(self, root):
        self.root = root;
        self.root.title("To-Do App");

        # List to hold all tasks
        self.tasks = [];

        # Create a frame
        self.frame = tk.Frame(self.root);
        self.frame.pack(padx=10, pady=10);

        # Add a task button
        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task);
        self.add_task_button.pack(side=tk.LEFT);

        # Text entry box
        self.task_entry = tk.Entry(self.frame, width=40);
        self.task_entry.pack(side=tk.LEFT, padx=5);

        # Listbox to display all tasks
        self.listbox = tk.Listbox(self.root, width=50, height=15);
        self.listbox.pack(pady=10, padx=10);

        # Add a delete button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task);
        self.delete_button.pack(pady=5);

    def add_task(self):
        task = self.task_entry.get();
        if task:
            self.tasks.append(task);
            self.listbox.insert(tk.END, task);
            self.task_entry.delete(0, tk.END);
        else:
            messagebox.showwarning("Warning", "Please enter a task!");

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0];
            self.listbox.delete(task_index);
            self.tasks.pop(task_index);
        except:
            messagebox.showwarning("Warning", "Please select a task to delete!");

if __name__ == "__main__":
    root = tk.Tk();
    app = ToDoApp(root);
    root.mainloop();



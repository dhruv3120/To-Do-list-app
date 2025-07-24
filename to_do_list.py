import tkinter as tk
from tkinter import messagebox

tasks = []

def add_tsk():
    tsk_text = task.get()
    if tsk_text:
        tasks.append(tsk_text)
        listbox.insert(tk.END, tsk_text)
        task.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showerror("Error", "Please select a task to remove")



app = tk.Tk()
app.title("TO DO LIST")
app.geometry("400x400")


task = tk.Entry(app, width=45)
task.pack(pady=20)


add_task = tk.Button(app, text="ADD TASK", command=add_tsk)
add_task.pack()


listbox = tk.Listbox(app, width=60)
listbox.pack(pady=40)


rmv_button = tk.Button(app, text="Remove Task", command=remove_task)
rmv_button.pack()


app.mainloop()

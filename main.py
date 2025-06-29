from tkinter import *

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(False)
        task_listbox.insert(END, f"☐ {task}")
        task_entry.delete(0, END)

def delete_task():
    sel = task_listbox.curselection()
    if sel:
        idx = sel[0]
        task_listbox.delete(idx)
        tasks.pop(idx)

def complete_task():
    sel = task_listbox.curselection()
    if sel:
        idx = sel[0]
        done = not tasks[idx]  
        tasks[idx] = done
        text = task_listbox.get(idx)[2:]
        prefix = "✓" if done else "☐"
        task_listbox.delete(idx)
        task_listbox.insert(idx, f"{prefix} {text}")
        task_listbox.selection_clear(0, END)

root = Tk()
root.title("TO DO LIST")
root.geometry("800x700")
root.config(bg='lightyellow')

Label(root, text="To Do List", bg='pink', font=('Bahnschrift', 26, 'bold underline')).pack()
task_entry = Entry(root, font=('Arial',16), width=22); task_entry.pack(pady=20)

Button(root, text="Add Task", font=('Arial',14), command=add_task, bg='lightblue').pack(pady=10)
task_listbox = Listbox(root, font=('Arial',16), width=22); task_listbox.pack(pady=20)

Button(root, text="Delete Task", font=('Arial',14), command=delete_task, bg='lightblue').pack(pady=10)
Button(root, text="Mark Completed", font=('Arial',14), command=complete_task, bg='lightgreen').pack(pady=10)

root.mainloop()
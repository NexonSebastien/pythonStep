import tkinter as tk

counter_id = None

def decompte(count=10):
    global counter_id
    lab['text'] = count
    if count > 0:
        counter_id = fen1.after(1000, decompte, count - 1)

def stop():
    if counter_id:
        fen1.after_cancel(counter_id)
        lab['text'] = "stop!"

fen1 = tk.Tk()

lab = tk.Label(fen1, text="")
lab.pack()

decompte()

fen1.mainloop()
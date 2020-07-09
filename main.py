from tkinter import Tk, Label
from time import sleep
from psutil import virtual_memory
from threading import Thread
template = """Свободно памяти: {} Мб
Используется: {} Мб"""

root = Tk()
root.title("Memory usage")
root.geometry('600x150')

label = Label(root, text=template, font=("Arial Bold", 32))
label.grid(column=0, row=0)

def update():
    sleep(1)
    while True:
        mem = virtual_memory()
        free = round(mem.free / 1000000)
        used = round(mem.used / 1000000)
        text = template.format(free, used)
        label.configure(text=text)
        sleep(1)

Thread(target=update, daemon=True).start()
try:
    root.mainloop()
except KeyboardInterrupt:
    exit(print())
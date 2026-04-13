import tkinter as tk
import os
import random
root = tk.Tk()
root.title("Кодировка.py")

file_read_gui = tk.Entry(root, font=("Arial", 24, "bold"))
file_read_gui.grid(row=4, column=0)

read_text = tk.Label(root, text="Расположения файла", font=("Arial", 24, "bold"))
read_text.grid(row=5, column=0)

save = tk.Label(root, height=6)
save.grid(row=3, column=0)

error = tk.Label(root, height=6)
error.grid(row=6, column=0)

key_gui = tk.Entry(root, font=("Arial", 24, "bold"))
key_gui.grid(row=7, column=0)

key_gui1 = tk.Label(root, text="Ключ", font=("Arial", 28, "bold"))
key_gui1.grid(row=8, column=0)

def Coded():
    error.config(text="Файл закодирован", font=("Arial", 20, "bold"), fg="black")
    root.after(1000, Clear)
def UnCoded():
    error.config(text="Файл раскодирован", font=("Arial", 20, "bold"), fg="black")
    root.after(1000, Clear)
def Error():
    error.config(text="Ошибка", height=3, font=("Arial", 20, "bold"), fg="red")
    root.after(1000, Clear)
def Clear():
    error.config(text="", height=3)
    save.config(text="", height=3)
    #кодируем
def Codirovka():
    global key_gui
    global file_read_gui
    key = []
    file_for_read = file_read_gui.get()
    key_1 = key_gui.get()
    for key_symv in key_1:
        key_symv = str(ord(key_symv))
        key.append(key_symv)
    key = "".join(key)
    try:
        key = int(key)
    except:
        Error()
    symv_s = []
    with open(file_for_read, "r", encoding="utf-8") as f:
        lines = f.read()
    for line in lines:
        for symv in line:
            #шифруем(важноважно, ord)
            symv = str(ord(symv)+int(key))
            symv = symv
            symv_s.append(symv)
    #соединитьпошифру
    symv_s = "0x"+(".0x".join(symv_s))
    with open(file_for_read, "w", encoding="utf-8") as f:
        f.write(symv_s)
    Coded()
    #раскодируем
def Read():
        global key
        global file_read_gui
        file_for_read = file_read_gui.get()
        key = []
        chikls = 0
        key_1 = key_gui.get()
        for key_symv in key_1:
            key_symv = str(ord(key_symv))
            key.append(key_symv)
        key = "".join(key)
        key = int(key)
        with open(file_for_read, "r+", encoding="utf-8") as f:
            symv_s = f.read()
        symv_r = []
        symv_s = symv_s.split(".0x")
        for symv in symv_s:
            chikls += 1
            if chikls == 1:
                symv = symv[2:]
            try:
                symv = round(int(symv)-int(key))
                #расшифровываем(важноважно)
                symv = chr(symv)
                symv_r.append(symv)
            except ValueError:
               Error()
            
        symv_r = "".join(symv_r)
        with open(file_for_read, "w", encoding="utf-8") as f:
            f.write(symv_r)
        UnCoded()
def Open():
    global file_read_gui
    file_for_read = file_read_gui.get()
    os.startfile(file_for_read)
cod = tk.Button(root, text="Кодировка выбранного файла",font=("Arial", 24, "bold"), command=Codirovka)
cod.grid(row=0, column=0)

recod = tk.Button(root, text="Раскодировка выбранного файла",font=("Arial", 24, "bold"), command=Read)
recod.grid(row=1, column=0)

open_file = tk.Button(root, text="Открыть файл",font=("Arial", 24, "bold"), command=Open)
open_file.grid(row=2, column=0)

root.mainloop()
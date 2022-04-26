from tkinter import *
from tkinter import messagebox # Окно сообщений
from tkinter import filedialog # Проводник 
import os
from datetime import datetime
from tkinter import ttk # стиль кнопок под ваше ОС

def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)

def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d') # формат даты Г М Д
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder): # существует ли такая директория
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Success', 'Сортировка выполнена успешно')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Выберите папку с фотографиями')
                    


root = Tk()
root.title('PhotoSort')
root.geometry('500x150+550+300')
root.iconbitmap('Ps.ico')

s = ttk.Style()
s.configure('my.TButton', font = ('Helvetica', 12))


frame = Frame(root, bg = 'orange', bd = 5) # рамка окна ввода и цвет ее
frame.pack(pady = 10, padx = 10, fill = X)


e_path = ttk.Entry(frame) # окно ввода
e_path.pack(side = LEFT, ipady = 2,expand = True, fill = X) # выравнивается по левому краю, растягиваться может

btn_dialog = ttk.Button(frame, text = 'Выбрать папку', command = choose_dir)
btn_dialog.pack(side = LEFT, padx = 5)

btn_start = ttk.Button(root, text = 'Start', style = 'my.TButton', command = f_start)
btn_start.pack()


root.mainloop()
# coding=windows-1251
import pyautogui
import time
import os
import PIL
import keyboard
from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab, ImageTk
from PIL import Image

#задержка, точность, нажать

#pyautogui.press('esc')

#pyautogui.press("win")

#pyautogui.click(173, 1059)

#file_path1 = 'Scrins/a.txt'
#with open(file_path1, 'r+', encoding='utf-8') as f:
# num = int(f.read())
#f.close()

#with open(file_path1, 'r+', encoding='utf-8') as f:
#        f.write(str(num))
#    f.close()

def click_png(name, s_time, toch, pres):
    root.withdraw()
    while 1:
        try:
            time.sleep(s_time)
            pyautogui.click(pyautogui.locateOnScreen(name, confidence=toch))
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.5)
    if pres != '' or pres != None:
        try:
            pyautogui.press(pres)
        except:
            root.after_idle(root.deiconify)
            a = 1
    root.after_idle(root.deiconify)

def open_file():
    path = "Scrins"
    path = os.path.realpath(path)
    os.startfile(path)

def load_image_noob():
    global choice_now
    global photo_image
#   global file_path1
    file_path = filedialog.askopenfilename()
    try:
        image = Image.open(file_path)
        image.save(f'Scrins/image{arr_button[choice_now]}.png')
    except:
        a = 1
    try:
        image_path = f"Scrins/image{arr_button[choice_now]}.png"
        image = Image.open(image_path)
        image = image.resize((528, 297), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        frame_image.config(image = photo_image)
    except:
        a = 1

def load_image_pro(a):
    global choice_now
    global photo_image
#   global file_path1
    try:
        im = ImageGrab.grabclipboard()
        im.save(f'Scrins/image{arr_button[choice_now]}.png','PNG')
    except:
        a = 1
    try:
        image_path = f"Scrins/image{arr_button[choice_now]}.png"
        image = Image.open(image_path)
        image = image.resize((528, 297), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        frame_image.config(image = photo_image)
    except:
        a = 1

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==86 and  ctrl: 
        load_image_pro(1)

def save_sett():
    global choice_now
    may = True
    try:
        delay = float(del_entry.get())
    except:
        may = False
        win_error = Tk()
        lable_error = Label(win_error, text = 'В задержку надо ввести число', font='Verdana 12')
        win_error.geometry('480x270')
        lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)    
    try:
        if float(acc_entry.get()) > 1:
            may = False
            win_error = Tk()
            lable_error = Label(win_error, text = 'В точность надо ввести число меньше 1', font='Verdana 12')
            win_error.geometry('480x270')
            lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)
        else:    
            accuracy = float(acc_entry.get())
    except:
        may = False
        win_error = Tk()
        lable_error = Label(win_error, text = 'В точность надо ввести число меньше 1', font='Verdana 12')
        win_error.geometry('480x270')
        lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)       
    try:
        a = 'йцукенгшщзхъэждлорпавыфячсмитьбю1234567890'
        c = True
        for i in range(len(a)):
            for j in range(len(key_entry.get())):
                if a[i] == key_entry.get()[j]:
                    may = False
                    win_error = Tk()
                    lable_error = Label(win_error, text = 'В .НАЖАТЬ. надо\n вести английсую букуву', font='Verdana 12')
                    win_error.geometry('480x270')
                    lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)
                    c = False
                    break
        if c:
            key = key_entry.get().lower()
        else:
            c = True
    except:
        may = False
        win_error = Tk()
        lable_error = Label(win_error, text = 'В .НАЖАТЬ. надо ввести английсую букуву', font='Verdana 12')
        win_error.geometry('480x270')
        lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)
    if may == True:
        try:
            arr_button[choice_now+1] = delay
            arr_button[choice_now+2] = accuracy
            arr_button[choice_now+3] = key
        except:
            win_error = Tk()
            lable_error = Label(win_error, text = 'Выбран неверный шаг', font='Verdana 12')
            win_error.geometry('480x270')
            lable_error.place(relx=0, rely=0, relwidth=1, relheight=1)
            
def remuve_button(button_rem):
    global choice_now
    global index_button
    i = 0
    indexxx = 0
    for i in range(len(arr_button)):
        if button_rem == arr_button[i]:
            arr_button[i-1].destroy()
            arr_button.pop(i-1)
            arr_button[i-1].destroy()
            arr_button.pop(i-1)
            try:
                os.remove(f"Scrins/image{arr_button[i-1]}.png")
                if arr_button[choice_now-2] == arr_button[i-1]:
                    frame_image.config(image = photo_image_green)
            except:
                i = i
            indexxx = arr_button[i - 1]
            arr_button.pop(i-1)
            arr_button.pop(i-1)
            arr_button.pop(i-1)
            arr_button.pop(i-1)
            index_button-=1    
            break
    if i < len(arr_button):   
        for i in range(i-1, len(arr_button)):
            if i == 0 or i % 6 == 0:
                arr_button[i].place(rely=(arr_button[i+2]-1)*0.1 , relwidth=1, relheight=0.1)
                arr_button[i].config(text = arr_button[i+2])
                arr_button[i+1].place(rely=(arr_button[i+2]-1)*0.1 + 0.01, relx=0.84, relwidth=0.135, relheight=0.08)
                try:
                    os.rename(f"Scrins/image{arr_button[i+2]}.png", f"Scrins/image{arr_button[i+2]-1}.png")
                except:
                    a = 1
                arr_button[i+2]-=1
                #image nado
                
def choice(button):
    global choice_now
    global photo_image
    global photo_image_green
    for i in range(len(arr_button)):
        if button == arr_button[i]:
            choice_now = i+2
            break
    try:
        image_path = f"Scrins/image{arr_button[choice_now]}.png"
        image = Image.open(image_path)
        image = image.resize((528, 297), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        frame_image.config(image = photo_image)
    except:
        frame_image.config(image = photo_image_green)
        
def creat_button():
    global index_button
    if index_button <= 9: 
        
        new_button = Button(frame_arr, text = index_button+1, command =lambda: choice(new_button),bg='#54784c', font='Verdana 12', fg = '#dde8da')
        new_button.place(rely=index_button*0.1 , relwidth=1, relheight=0.1)
    
        arr_button.append(new_button)
    
        new_button_rem = Button(frame_arr,text='X', command=lambda: remuve_button(new_button_rem), bg='#86ab7d', font='Verdana 12', fg = '#dde8da')
        new_button_rem.place(rely=index_button*0.1 + 0.01, relx=0.84, relwidth=0.135, relheight=0.08)
        
        arr_button.append(new_button_rem)
    
        arr_button.append(index_button)
        arr_button.append(0)
        arr_button.append(0)
        arr_button.append(None)
    
        index_button+=1

def start():
    for i in range(len(arr_button)):
        if i == 0 or i % 6 == 0:
            click_png(f"Scrins/image{arr_button[i+2]}.png",arr_button[i+3],arr_button[i+4],arr_button[i+5])
            
##################################################################################################################

choice_now = 2
num = 0
delay = float()
accuracy = float()
key = str()
arr_button = []
index_button = 0

root = Tk()

image_path = f"Scrins/photo_image/image.png"
image = Image.open(image_path)
image = image.resize((528, 297), Image.Resampling.LANCZOS)
photo_image = ImageTk.PhotoImage(image)

image_path_green = f"Scrins/photo_image/image0.png"
image_green = Image.open(image_path_green)
image_green = image_green.resize((528, 297), Image.Resampling.LANCZOS)
photo_image_green = ImageTk.PhotoImage(image_green)

root.title("Avto Start++")
root.geometry('960x540')
root.resizable(width=False, height=False)
root.configure(bg='#273823')

root.bind('<Key>', _onKeyRelease, '+')

ramka = Label(root, bg='black')
ramka.place(relx=0.345, rely=0.14, relwidth=0.56, relheight=0.57)

frame_image = Label(root, bg='#121a10', image = None)
frame_image.place(relx=0.35, rely=0.15, relwidth=0.55, relheight=0.55)

frame_arr = Frame(root, bg='#54784c')
frame_arr.place(relx=0.05, rely=0.15, relwidth=0.2, relheight=0.7)

image_button = Button(root, text="Выбрать\nизоброжение", command=load_image_noob, bg='#54784c', font='Verdana 12', fg = '#dde8da')
image_button.place(relx=0.35, rely=0.825, relwidth=0.15, relheight=0.1)

creat_button = Button(root, text="+", command=creat_button, bg='#54784c', font='Verdana 12', fg = '#dde8da')
creat_button.place(relx=0.02, rely=0.15, relwidth=0.03, relheight=0.05)

start_button = Button(root, command=start, text="Начать", bg='#54784c', font='Verdana 12', fg = '#dde8da')
start_button.place(relx=0.1, rely=0.89, relwidth=0.1, relheight=0.075)

del_entry = Entry(root, bg='white')
del_entry.place(relx=0.7, rely=0.775, relwidth=0.03, relheight=0.05)
del_label = Label(text = 'Задержка:', font='Verdana 12', bg='#273823', fg = '#dde8da')
del_label.place(relx=0.59, rely=0.775, relwidth=0.1, relheight=0.05)

acc_entry = Entry(root, bg='white')
acc_entry.place(relx=0.7, rely=0.85, relwidth=0.03, relheight=0.05)
acc_label = Label(text = 'Точность:', font='Verdana 12', bg='#273823', fg = '#dde8da')
acc_label.place(relx=0.592, rely=0.85, relwidth=0.1, relheight=0.05)

key_entry = Entry(root, bg='white')
key_entry.place(relx=0.7, rely=0.925, relwidth=0.03, relheight=0.05)
key_label = Label(text = 'Нажать:', font='Verdana 12', bg='#273823', fg = '#dde8da')
key_label.place(relx=0.6, rely=0.925, relwidth=0.1, relheight=0.05)

save_button = Button(root, text = 'Сохранть', command = save_sett,bg='#54784c', font='Verdana 12', fg = '#dde8da')
save_button.place(relx=0.8, rely=0.835, relwidth=0.1, relheight=0.08)


root.mainloop()
#Math Symbol App
import pyautogui as pg 
import time
import pyperclip as pc
from tkinter import *
import tkinter.font as font
import winsound
lst1 = ['α', 'β', 'δ', 'ε', 'θ', 'λ', 'μ', 'π', 'φ', 'ψ', 'Ω','∫','∧','∨','∮','∊','∅','√','∩','÷','⟂','≈']

root = Tk()
root.geometry("645x200")
root.resizable(0,0)
root.title("Mathsymbols")
root.configure(bg='black')
def Button0com():
    winsound.Beep(330,500)
    pc.copy(lst1[0])
    time.sleep(3)
    pg.hotkey("ctrl","v")

Button0 = Button(root,text = lst1[0],command = Button0com,fg = "White",bg = "Blue")
myfont = font.Font(size = 25)
Button0['font'] = myfont
Button0.place(x = 0,y = 0)
def Button1com():
    winsound.Beep(350,500)
    pc.copy(lst1[1])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button1 = Button(root,text = lst1[1],command = Button1com,fg = "White",bg = "Blue")
Button1['font'] = myfont
Button1.place(x = 60,y = 0)
#Button1.pack()
def Button2com():
    winsound.Beep(370,500)
    pc.copy(lst1[2])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button2 = Button(root,text = lst1[2],command = Button2com,fg = "White",bg = "Blue")
Button2['font'] = myfont
Button2.place(x = 120,y=0)
#Button2.pack()
def Button3com():
    winsound.Beep(390,500)
    pc.copy(lst1[3])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button3 = Button(root,text = lst1[3],command = Button3com,fg = "White",bg = "Blue")
Button3['font'] = myfont
Button3.place(x = 180,y = 0)
def Button4com():
    winsound.Beep(410,500)
    pc.copy(lst1[4])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button4 = Button(root,text = lst1[4],command = Button4com,fg = "White",bg = "Blue")
Button4['font'] = myfont
Button4.place(x = 220,y = 0)
def Button5com():
    winsound.Beep(430,500)
    pc.copy(lst1[5])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button5 = Button(root,text = lst1[5],command = Button5com,fg = "White",bg = "Blue")
Button5['font'] = myfont
Button5.place(x = 280,y = 0)
def Button6com():
    winsound.Beep(450,500)
    pc.copy(lst1[6])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button6 = Button(root,text = lst1[6],command = Button6com,fg = "White",bg = "Blue")
Button6['font'] = myfont
Button6.place(x = 340,y = 0)
def Button7com():
    winsound.Beep(470,500)
    pc.copy(lst1[7])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button7 = Button(root,text = lst1[7],command = Button7com,fg = "White",bg = "Blue")
Button7['font'] = myfont
Button7.place(x = 400,y = 0)
def Button8com():
    winsound.Beep(490,500)
    pc.copy(lst1[8])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button8 = Button(root,text = lst1[8],command = Button8com,fg = "White",bg = "Blue")
Button8['font'] = myfont
Button8.place(x = 460,y = 0)
def Button9com():
    winsound.Beep(510,500)
    pc.copy(lst1[9])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button9 = Button(root,text = lst1[9],command = Button9com,fg = "White",bg = "Blue")
Button9['font'] = myfont
Button9.place(x = 520,y = 0)
def Button10com():
    winsound.Beep(530,500)
    pc.copy(lst1[10])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button10 = Button(root,text = lst1[10],command = Button10com,fg = "White",bg = "Blue")
Button10['font'] = myfont
Button10.place(x = 580,y = 0)
def Button11com():
    winsound.Beep(350,500)
    pc.copy(lst1[11])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button11 = Button(root,text = lst1[11],command = Button11com,fg = "White",bg = "Blue")
Button11['font'] = myfont
Button11.place(x = 0,y = 100)
def Button12com():
    winsound.Beep(370,500)
    pc.copy(lst1[12])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button12 = Button(root,text = lst1[12],command = Button12com,fg = "White",bg = "Blue")
Button12['font'] = myfont
Button12.place(x = 40,y = 100)
def Button13com():
    winsound.Beep(390,500)
    pc.copy(lst1[13])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button13 = Button(root,text = lst1[13],command = Button13com,fg = "White",bg = "Blue")
Button13['font'] = myfont
Button13.place(x = 100,y = 100)
def Button14com():
    winsound.Beep(410,500)
    pc.copy(lst1[14])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button14 = Button(root,text = lst1[14],command = Button14com,fg = "White",bg = "Blue")
Button14['font'] = myfont
Button14.place(x = 160,y = 100)
#15
def Button15com():
    winsound.Beep(430,500)
    pc.copy(lst1[15])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button15 = Button(root,text = lst1[15],command = Button15com,fg = "White",bg = "Blue")
Button15['font'] = myfont
Button15.place(x = 230,y = 100)
#16
def Button16com():
    winsound.Beep(450,500)
    pc.copy(lst1[16])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button16 = Button(root,text = lst1[16],command = Button16com,fg = "White",bg = "Blue")
Button16['font'] = myfont
Button16.place(x = 290,y = 100)
#17
def Button17com():
    winsound.Beep(470,500)
    pc.copy(lst1[17])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button17 = Button(root,text = lst1[17],command = Button17com,fg = "White",bg = "Blue")
Button17['font'] = myfont
Button17.place(x = 340,y = 100)
#18
def Button18com():
    winsound.Beep(490,500)
    pc.copy(lst1[18])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button18 = Button(root,text = lst1[18],command = Button18com,fg = "White",bg = "Blue")
Button18['font'] = myfont
Button18.place(x = 400,y = 100)
#19
def Button19com():
    winsound.Beep(510,500)
    pc.copy(lst1[19])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button19 = Button(root,text = lst1[19],command = Button19com,fg = "White",bg = "Blue")
Button19['font'] = myfont
Button19.place(x = 460,y = 100)
#20
def Button20com():
    winsound.Beep(530,500)
    pc.copy(lst1[20])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button20 = Button(root,text = lst1[20],command = Button20com,fg = "White",bg = "Blue")
Button20['font'] = myfont
Button20.place(x = 520,y = 100)
def Button21com():
    winsound.Beep(550,500)
    pc.copy(lst1[21])
    time.sleep(3)
    pg.hotkey("ctrl","v")
Button21 = Button(root,text = lst1[21],command = Button21com,fg = "White",bg = "Blue")
Button21['font'] = myfont
Button21.place(x = 580,y = 100)

root.mainloop()
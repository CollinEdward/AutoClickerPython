import pyautogui as pg
import keyboard
import tkinter
from tkinter import *
import hotkey_settings


root = Tk()
root.title("AutoClicker")
root.geometry("1000x300")



def what_is_hotkey():
    button_hotkey = Label(root, text="Your Right click hotkey is " +  hotkey_settings.left_hotkey).pack()
what_is_hotkey()

def AutoClicker():
    while 1:
        while keyboard.is_pressed(hotkey_settings.left_hotkey):
            pg.doubleClick(0,0)


        while keyboard.is_pressed(hotkey_settings.right_hotkey):
            pg.rightClick(0,0)

button_activate = Button(root, text="Activate AutoClicker", command=AutoClicker).pack()


root.mainloop()


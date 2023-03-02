from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import random

var = 0
pixnum = 700
piynum = 280
times = 0
noom = 0
place = 0
al_val = []
al_val2 = []
stop = 0

def paste():
    global noom, place, al_val, al_val2
    place = 0
    while noom != 0:
        xval = al_val[place]
        yval = al_val2[place]
        click(xval, yval)
        noom = noom - 1
        place = place + 1 
    pyautogui.moveTo(0,0)
    time.sleep(3.5)

def check2():
    global place, al_val, al_val2
    place = 0
    print(al_val)
    print(al_val2)
    xval = al_val[place]
    yval = al_val2[place]
    while pyautogui.pixel(xval,yval)[0] == 191:
        pass
    paste()

def copy():
    global pixnum, piynum, times, noom, al_val, al_val2
    noom = 0
    piynum = 280
    pixnum = 700
    al_val.clear()
    al_val2.clear()
    times = 0
    for i in range(36):
        if times == 6:
            times = 0
            piynum = piynum + 100
            pixnum = 700 
        if pyautogui.pixel(pixnum,piynum)[0] == 191:
            al_val.append(pixnum)
            al_val2.append(piynum)
            noom = noom + 1                   
        pixnum = pixnum + 100
        times = times + 1
    al_val_length = len(al_val)
    if al_val_length == 0:
        check()
    else:
        check2()
    


def check():
    global pixnum, piynum, times, var
    while var == 0:
        piynum = 280
        for i in range(36):
            if times == 6:
                times = 0
                piynum = piynum + 100
                pixnum = 700 
            if pyautogui.pixel(pixnum,piynum)[0] == 191:
                var = 1
                copy()
                break
            pixnum = pixnum + 100
            times = times + 1

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

while True:
    timeforplay = random.randint(25,27)
    for i in range(timeforplay):
        check()
        var = 0
    if keyboard.is_pressed('esc'):
        break
    time.sleep(20)
    keyboard.press("alt")
    time.sleep(0.05)
    rclick(0,0)
    time.sleep(.05)
    click(1355, 720)
    keyboard.release("alt")
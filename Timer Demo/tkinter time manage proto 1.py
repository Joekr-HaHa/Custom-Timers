from tkinter import *
import tkinter
import random
import time
from tkinter import font as tkFont
from threading import Thread
from tkinter import ttk
from ttkthemes import themed_tk

#tk=tkinter.Tk()
tk=themed_tk.ThemedTk()

tk.get_themes()
tk.set_theme("radiance")
helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
var1="History"
n=IntVar()
n.set(3600)
x=3600
class Tasks():
    def __init__(self,window,lesson,time):
        self.window=window
        self.lesson=lesson
        self.time=time
        self.done=False
    def countdown(self):
            if self.done==False:
                self.window['font']=helv36
                self.time-=0.5
                if self.time>0 and self.time>=3600:
                    self.window['text']=("{} Hrs {} Mins {} Secs left for {}").format(((self.time)//60**2),((self.time-(3600*(self.time//60**2)))//60),(self.time%60),self.lesson)
                    tk.after(1000,self.countdown)
                elif self.time>=0:
                    
                    self.window['text']=("{} mins {} secs left for {}").format((self.time//60),(self.time%60),self.lesson)
                    
                    tk.after(1000,self.countdown)
                else:
                    self.window['text']=("You have finished {}!".format(self.lesson))
            else:
                self.window['text']='Timer Paused'
                tk.after(1000,self.countdown)
                



c1Pressed=IntVar()
c2Pressed=IntVar()
c3Pressed=IntVar()
hist=False
mat=False
comp=False

def check_button(win,button):
    if button.get()==1:
        win.done=True
    elif button.get()==0:
        win.done=False

    
def start_his():
    global his,c1Pressed,hist
    c1Pressed=IntVar()
    c1=Checkbutton(tk,variable=c1Pressed\
               ,onvalue=1,offvalue=0,height=2,width=40)
    his=Tasks(c1,"History",14400)
    his.countdown()
    thread1=Thread(target=his.countdown)
    thread1.start()
    thread4=Thread(target=check_if_pressed)
    thread4.start()
    hist=True
    c1.pack()
    
    
def start_cs():
    global cs,c2Pressed,comp
    c2Pressed=IntVar()
    c2=Checkbutton(tk,variable=c2Pressed\
               ,onvalue=1,offvalue=0,height=2,width=40)
    cs=Tasks(c2,"Computer Science",7200)
    cs.countdown()
    thread2=Thread(target=cs.countdown)
    thread2.start()
    c2.pack()
    comp=True
def start_ma():
    global ma,c3Pressed,mat
    c3Pressed=IntVar()
    c3=Checkbutton(tk,variable=c3Pressed\
               ,onvalue=1,offvalue=0,height=2,width=40)
    ma=Tasks(c3,"Mathematics",7200)
    ma.countdown()
    thread3=Thread(target=ma.countdown)
    thread3.start()
    c3.pack()
    mat=True

''''def start_sub():
    c4Pressed=IntVar()
    c4=Checkbutton(tk,variable=c4Pressed\
               ,onvalue=1,offvalue=0,height=2,width=40)
    i=Tasks(c4,"",3600)
    i.countdown()
    thread4=Thread(target=i.countdown)
    thread4.start()
    c4.pack()'''
b1=Button(tk,text="Start History",command=start_his).pack()
b2=Button(tk,text="Start Computer Science",command=start_cs).pack()
b3=Button(tk,text="Start Mathematics",command=start_ma).pack()
#b4=Button(tk,text="Start Subject",command=start_sub).pack()
s=Scrollbar(tk).pack(side=RIGHT,fill=Y)

def check_if_pressed():
    global hist,mat,comp
    while True:
        if comp==True:
            check_button(cs,c2Pressed)
        if hist==True:
            check_button(his,c1Pressed)
        if mat==True:
            check_button(ma,c3Pressed)

tk.mainloop()



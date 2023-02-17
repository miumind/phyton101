from tkinter import *
from tkinter import ttk #theme of Tk
from tkinter import messagebox
import tkinter.messagebox
import tkinter as tk

GUI = Tk()
GUI.title('ตารางงาน')#ชื่อโปรแกรม
GUI.geometry('910x250')#ขนาดหน้าจอโปรแกรม
GUI.config(bg='White')#สีพื้นหลัง
L1=Label(GUI,text='ตารางงาน',font=('Angsana New',30,'bold'),fg='blue',bg='White')
L1.place(x=400,y=20)

### 1 ###
def display_text1():
    tkinter.messagebox.showinfo("วันจันทร์", "พบลูกค้า A 10:00น.")
FB1 = LabelFrame(GUI,text='February')
FB1.place(x=0,y=100)
button = Button(FB1, text="วันจันทร์\n13",command=display_text1)
button.config(bg="yellow", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 2 ###
def display_text2():
    tkinter.messagebox.showinfo("วันอังคาร", "พบลูกค้า B 10:00น.\nพบลูกค้า C 14:00น.")
FB2 = LabelFrame(GUI,text='February')
FB2.place(x=130,y=100)    
button = Button(FB2, text="วันอังคาร\n14",command=display_text2)
button.config(bg="magenta", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 3 ###
def display_text3():
    tkinter.messagebox.showinfo("วันพุธ", "Office")
FB3 = LabelFrame(GUI,text='February')
FB3.place(x=260,y=100)    
button = Button(FB3, text="วันพุธ\n15",command=display_text3)
button.config(bg="lime", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 4 ###
def display_text4():
    tkinter.messagebox.showinfo("วันพฤหัสบดี", "ประชุม แผนก 10:00น.\nประชุม บริษัท 14:00น.")
FB4 = LabelFrame(GUI,text='February')
FB4.place(x=390,y=100)    
button = Button(FB4, text="วันพฤหัสบดี\n16",command=display_text4)
button.config(bg="orange", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 5 ###
def display_text5():
    tkinter.messagebox.showinfo("วันศุกร์", "อบรม\n9:30-16:30น.")
FB5 = LabelFrame(GUI,text='February')
FB5.place(x=520,y=100)     
button = Button(FB5, text="วันศุกร์\n17",command=display_text5)
button.config(bg="cyan", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 6 ###
def display_text6():
    tkinter.messagebox.showinfo("วันเสาร์", "Activity Day\n8:30-12:00น.")
FB6 = LabelFrame(GUI,text='February')
FB6.place(x=650,y=100)   
button = Button(FB6, text="วันเสาร์\n18",command=display_text6)
button.config(bg="purple", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########
### 7 ###
def display_text7():
    tkinter.messagebox.showinfo("วันอาทิตย์", "Holiday")
FB7 = LabelFrame(GUI,text='February')
FB7.place(x=780,y=100)      
button = Button(FB7, text="วันอาทิตย์\n19",command=display_text7)
button.config(bg="red", fg="black",font=('Angsana New',15,'bold'), width=10, height=1)
button.config(bd=5)
button.pack(ipadx=5,ipady=5,padx=10,pady=10)
########

GUI.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import socket
from tkinter import messagebox
from pandastable import Table
import pandas as pd
import tkinter as tk

top = Tk()  
top.title("RC BOT")
top.geometry("600x600+0+0")
myFont = ('Helvetica',20,'bold')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('bgimage.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(top, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


#record page
class RECORD:
    def __init__(root):
              root=Tk()
              root.title("RECORD")
              root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
              myFont = ('Helvetica',15,'bold')
              root.configure(bg='black')
              img=Image.open('bg.png')

              def Live():
                  try:
                      c=socket.socket()
                      c.connect(('192.1168.43.31',80))
                      messagebox.showinfo("BOT CONNECTED","System is connected to BOT...")
                      recordl=Toplevel()
                      recordl.title("LIVE RECORD")
                      recordl.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                      myFont = ('Helvetica',15,'bold')
                      recordl.configure(bg='black')
                      
                      def resize_image(event):
                            new_width = event.width
                            new_height = event.height
                            image = copy_of_image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label.config(image = photo)
                            label.image = photo #avoid garbage collection
                      image = Image.open('newkeyboard3.png')
                      copy_of_image = image.copy()
                      photo = ImageTk.PhotoImage(image)
                      label = ttk.Label(recordl, image = photo)
                      label.bind('<Configure>', resize_image)
                      label.pack(fill=BOTH, expand = YES)
                      
                      hu=Button(recordl,text='HUMIDITY',bg='#ffffff',fg='#000000',font=myFont)
                      hu.place(x=100,y=150)
                      hh=Button(recordl,text='HEAT',bg='#ffffff',fg='#000000',font=myFont)
                      hh.place(x=500,y=150)
                      ul=Button(recordl,text='ULTRASONIC',bg='#ffffff',fg='#000000',font=myFont)
                      ul.place(x=900,y=150)
                      Gas=Button(recordl,text='GAS',bg='#ffffff',fg='#000000',font=myFont)
                      Gas.place(x=1200,y=150)
                  except:
                         messagebox.showerror("NETWORK ERROR","System should connect to N/W")
                  
                  
              Live = Button(root, text = 'Live records',bg='#ffffff',fg='#000000', font=myFont,command=Live)
              Live.place(x=100,y=150)
              

              def Previous():
                  recordp=Toplevel()
                  recordp.title("PREVIOUS RECORD")
                  recordp.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                  myFont = ('Helvetica',15,'bold')
                  recordp.configure(bg='black')
                  def Heat():
                      df=pd.read_csv('Heat.csv')
                      root = Toplevel()
                      root.title("HEAT")
                      
                      print(df)
                      pt = Table(root,dataframe=df)

                      pt.show()

                  def Humidity():
                      df=pd.read_csv('Humidity.csv')
                      root = Toplevel()
                      root.title("HUMIDITY")
                      
                      print(df)
                      pt = Table(root,dataframe=df)

                      pt.show()


                  def Gas():
                      df=pd.read_csv('Gas.csv')
                      root = Toplevel()
                      root.title("GAS")
                      
                      print(df)
                      pt = Table(root,dataframe=df)

                      pt.show()


                  def resize_image(event):
                        new_width = event.width
                        new_height = event.height
                        image = copy_of_image.resize((new_width, new_height))
                        photo = ImageTk.PhotoImage(image)
                        label.config(image = photo)
                        label.image = photo #avoid garbage collection
                  image = Image.open('newkeyboard3.png')
                  copy_of_image = image.copy()
                  photo = ImageTk.PhotoImage(image)
                  label = ttk.Label(recordp, image = photo)
                  label.bind('<Configure>', resize_image)
                  label.pack(fill=BOTH, expand = YES)

                  hu=Button(recordp,text='HUMIDITY',bg='#ffffff',fg='#000000',font=myFont,command=Humidity)
                  hu.place(x=100,y=150)
                  hh=Button(recordp,text='HEAT',bg='#ffffff',fg='#000000',font=myFont,command=Heat)
                  hh.place(x=500,y=150)
                  ul=Button(recordp,text='ULTRASONIC',bg='#ffffff',fg='#000000',font=myFont)
                  ul.place(x=900,y=150)
                  Gas=Button(recordp,text='GAS',bg='#ffffff',fg='#000000',font=myFont,command=Gas)
                  Gas.place(x=1200,y=150)
              Previous = Button(root,text='Previous Record', bg='#ffffff',fg='#000000',font=myFont,command=Previous)
              
              Previous.place(x=700,y=150)
              '''tv=ttk.Treeview(root,columns=(1,2,3),show='headings',height='5')
              tv.pack()
              tv.heading(1,text='name')
              tv.heading(2,text='age')
              tv.heading(3,text='email')'''

#about us page
class ABOUT_PROJECT:
    def __init__(root):
              root=Toplevel()
              root.title("ABOUT PROJECT")
              root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
              myFont = ('Helvetica',15,'bold')
              #root.configure(bg='white')
              def resize_image(event):
                    new_width = event.width
                    new_height = event.height
                    image = copy_of_image.resize((new_width, new_height))
                    photo = ImageTk.PhotoImage(image)
                    label.config(image = photo)
                    label.image = photo #avoid garbage collection'''
              image = Image.open('bgimage.png')
              copy_of_image = image.copy()
              photo = ImageTk.PhotoImage(image)
              #label = ttk.Label(root, image = photo)
              label.bind('<Configure>', resize_image)
              label.pack(fill=BOTH, expand = YES)
#details
class DETAILS:
    def __init__(root):
              root=Toplevel()
              root.title("DETAILS")
              root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
              myFont = ('Helvetica',15,'bold')
              #root.configure(bg='white')
              def resize_image(event):
                    new_width = event.width
                    new_height = event.height
                    image = copy_of_image.resize((new_width, new_height))
                    photo = ImageTk.PhotoImage(image)
                    label.config(image = photo)
                    label.image = photo #avoid garbage collection'''
              image = Image.open('AbtS.png')
              copy_of_image = image.copy()
              photo = ImageTk.PhotoImage(image)
              label = ttk.Label(root, image = photo)
              label.bind('<Configure>', resize_image)
              label.pack(fill=BOTH, expand = YES)
#others
class ABOUT_US:
    def __init__(root):
              root=Toplevel()
              root.title("ABOUT PROJECT")
              root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
              myFont = ('Helvetica',15,'bold')
              #root.configure(bg='white')
              def resize_image(event):
                    new_width = event.width
                    new_height = event.height
                    image = copy_of_image.resize((new_width, new_height))
                    photo = ImageTk.PhotoImage(image)
                    label.config(image = photo)
                    label.image = photo #avoid garbage collection'''
              image = Image.open('AbtUs.png')
              copy_of_image = image.copy()
              photo = ImageTk.PhotoImage(image)
              label = ttk.Label(root, image = photo)
              label.bind('<Configure>', resize_image)
              label.pack(fill=BOTH, expand = YES)              
Record = Button(top, text = 'Record',bg='#ffffff',fg='#000000', font=myFont, command=RECORD)
Record.place(x=100,y=150)

About_us = Button(top, text = 'About Project',bg='#ffffff',fg='#000000', font=myFont, command=ABOUT_PROJECT)
About_us.place(x=400,y=150)

Detail = Button(top, text = 'Details',bg='#ffffff',fg='#000000', font=myFont, command=DETAILS)
Detail.place(x=700,y=150)

Others = Button(top, text = 'About us',bg='#ffffff',fg='#000000', font=myFont, command=ABOUT_US)
Others.place(x=1000,y=150)

top.mainloop()

# скачать с ютуба
#from importlib.resources import path
#import pytube
# from pytube import YouTube
# from tkinter import *



# #YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# path = r'Python-task\sem_9'
# yt.streams.filter(progressive=True, file_extension='mp4')
# yt.streams.order_by('resolution')
# yt.streams.desc()
# #yt.streams.first()
# yt.streams.first().download(path)


# # vid = input('вставьте ссылку на видео: ')
# # yt = YouTube(vid)
# # path = input('напишите адрес папки куда скачать: ')
# # yt.streams.filter(progressive=True, file_extension='mp4')
# # yt.streams.order_by('resolution')
# # yt.streams.desc()
# # #yt.streams.first()
# # yt.streams.first().download(path)

# def clicked():  
#     res = "Привет {}".format(txt.get())  
#     lbl.configure(text=res)  
  
  
# window = Tk()  
# window.title("Добро пожаловать в приложение YouTube")  
# window.geometry('400x250')  
# lbl = Label(window, text="вставьте ссылку на видео:")  
# lbl.grid(column=0, row=0)  
# txt = Entry(window,width=10)  
# txt.grid(column=1, row=0)  
# btn = Button(window, text="Клик!", bg="white", fg="red", command=clicked)  
# btn.grid(column=2, row=0)  
# window.mainloop()

# import tkinter as tk
# from pytube import YouTube
 
 
# def Download_Video():     
#     url =YouTube(str(link.get()))
#     video = url.streams.first()
#     video.download()
#     tk.Label(window, text = 'Ваше видео загружено!', font = 'arial 15',fg="White",bg="red").place(x= 10 , y = 140)  
 
# window = tk.Tk()
# window.geometry("600x200")
# window.config(bg="white")
# window.resizable(width=False,height=False)
# window.title('YouTube')
 
# link = tk.StringVar()
# tk.Label(window,text = 'YouTube', font ='arial 20 bold',fg="red",bg="White").pack()
# tk.Label(window, text = 'Вставьте сюда ссылку на YouTube:', font = 'arial 20 bold',fg="red",bg="White").place(x= 5 , y = 60)
# link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="lightgreen").place(x = 5, y = 100)
# tk.Button(window,text = 'СКАЧАТЬ ВИДЕО', font = 'arial 15 bold' ,fg="red",bg = 'White', padx = 2,command=Download_Video).place(x=385 ,y = 140)
 
# window.mainloop()


#https://www.youtube.com/watch?v=XP34I7CNRMo



import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():
     
    # заголовок
	head_label = Label(root, text="YouTube",padx=5,pady=5,font="white",bg="white",fg="red")
	head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)
    # меню1
	link_label = Label(root,text="Ссылка на YouTube :",bg="salmon",pady=2,padx=2)
	link_label.grid(row=2,column=0,pady=2,padx=2)    
	root.linkText = Entry(root,	width=34,textvariable=video_Link,font="Arial 12")
	root.linkText.grid(row=2,column=1,pady=2,padx=2,columnspan=2)
    #меню2
	destination_label = Label(root,text="Путь скачивания :",bg="salmon",pady=5,padx=9)
	destination_label.grid(row=3,column=0,pady=5,padx=5)
	root.destinationText = Entry(root,width=25,textvariable=download_Path,font="Arial 12")
	root.destinationText.grid(row=3,column=1,pady=5,padx=5)
    #выбрать папку для скачивания
	browse_B = Button(root,text="Выбрать",command=Browse,width=10,bg="bisque",relief=GROOVE)
	browse_B.grid(row=3,column=2,pady=1,padx=1)
    #кнопка скачивания
	Download_B = Button(root,text="Скачать видео",command=Download,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
	Download_B.grid(row=4,column=1,pady=25,padx=25)
# сохранить видео

def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")
	download_Path.set(download_Directory)

def Download():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.first()
	videoStream.download(download_Folder)
	messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n"+ download_Folder)
root = tk.Tk()
root.geometry("600x300")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()


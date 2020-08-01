from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import recover

top = Tk()
top.title("Flash Unveiled")
top.geometry("540x360")

labelframe1 = LabelFrame(top, text="Select the disk")
labelframe1.pack(fill="both", expand="yes", padx=10, pady=10)


toplabel = Label(labelframe1, text="Select the path of drive :")
toplabel.pack()

drive = ""


def drivepath():
    global drive
    drive = fd.askopenfilename(initialdir='/dev', title='select the drive')
    drivelabel.configure(text=drive)


drivebutton = Button(labelframe1, text='Select drive', command=drivepath)
drivebutton.pack()
drivelabel = Label(labelframe1, text=drive, borderwidth=2, relief="groove", width=40)
drivelabel.pack(pady=(5, 0))


def clear_1():
    drivelabel.configure(text="")


clear1 = Button(labelframe1, text="Clear", command=clear_1)
clear1.pack(side=RIGHT, padx=(0, 95))

labelframe2 = LabelFrame(top, text="Save path")
labelframe2.pack(fill="both", expand="yes", padx=10, pady=(5, 15))

bottomlabel = Label(labelframe2, text="Select the output path:")
bottomlabel.pack()

save = ""


def savepath():
    global save
    save = fd.askdirectory()
    savelabel.configure(text=save)


savebutton = Button(labelframe2, text='Select save path', command=savepath)
savebutton.pack()
savelabel = Label(labelframe2, text=save, borderwidth=2, relief="groove", width=40)
savelabel.pack(pady=(5, 0))


def clear_2():
    savelabel.configure(text="")


clear2 = Button(labelframe2, text="Clear", comman=clear_2)
clear2.pack(side=RIGHT, padx=(0, 95))


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Done")
    label = Label(popup, text=msg)
    label.pack(side="top", padx=10, pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack(pady=(0, 10))
    popup.mainloop()


def start():
    # call the main program here with arg as (drive) and (save)
    messagebox.showinfo('Message', "Scanning has started. Please wait!")
    recover.main(drive, save)
    messagebox.showinfo('Message', "Scanning has ended and files are recovered")
    top.destroy()


scanbutton = Button(top, text="Scan", command=start)
scanbutton.pack(pady=(0, 20), padx=(0, 20), side=RIGHT)

top.mainloop()

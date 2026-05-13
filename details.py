from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+230+220")
        self.root.config(bg="white")

        # ================= TITLE =================
        lbl_title = Label(
            self.root,
            text="ROOM BOOKING DETAILS",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.pack(side=TOP, fill=X)

        # ================= LOGO =================
        img = Image.open("logo.png")
        img = img.resize((50, 50), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg, bg="white")
        lbl_img.place(x=5, y=2)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=0, y=55, width=1295, height=655)

        self.showDatarame = Frame(main_frame, bd=4, relief=RIDGE, bg="white")
        self.showDatarame.place(x=450, y=5, width=300, height=260)

        # ================= LEFT FRAME =================
        labelframeleft = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Room Booking Details",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black"
        )
        labelframeleft.place(x=5, y=5, width=425, height=490)





if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop() 
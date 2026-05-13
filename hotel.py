from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        screen_width = self.root.winfo_screenwidth()
        #############1st image###################
        img1 = Image.open("hotel1.jpg")
        img1 = img1.resize((screen_width, 250), Image.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.pack(side=TOP, fill=X)

        ###############logo##################
        
        img2 = Image.open("logo.png")
        img2 = img2.resize((250, 250), Image.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=250, height=250)

        ###############title###################
        lbl_title= Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font =("times new roman",40,"bold"),bg="white",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=250,width=1750,height=50)

        ################### main frame ##############
        main_frame = Frame(self.root,bd = 4, relief= RIDGE)
        main_frame.place(x=0, y=300, width=1750, height=800)

        #################menu###########################
        lbl_menu= Label(main_frame, text="MENU", font =("times new roman",20,"bold"),bg="white",fg="gold",bd=4,relief=RIDGE)
        lbl_menu .place(x=0,y=0,width=230)

        ################### button frame ##############
        btn_frame = Frame(main_frame,bd = 4, relief= RIDGE)
        btn_frame.place(x=0, y=35, width=230)

        cust_btn = Button(btn_frame,
                  text="CUSTOMER",
                  command=self.cust_details,
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="gold", bd=0, cursor="hand2")

        cust_btn.pack(fill="x")

        room_btn = Button(btn_frame,
                  text="ROOM",
                  command=self.roombooking,
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="gold", bd=0, cursor="hand2")

        room_btn.pack(fill="x")

        details_btn = Button(btn_frame,
                  text="DETAILS",
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="gold", bd=0, cursor="hand2")

        details_btn.pack(fill="x")

        report_btn = Button(btn_frame,
                  text="REPORT",
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="gold", bd=0, cursor="hand2")

        report_btn.pack(fill="x")

        logout_btn = Button(btn_frame,
                  text="LOG OUT",
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="gold", bd=0, cursor="hand2")

        logout_btn.pack(fill="x")

        ###################Right side image#######################
        img3 = Image.open("img3.jpg")
        screen_width = self.root.winfo_screenwidth()

        img3 = img3.resize((screen_width - 230, 800), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=230, y=304 , width=screen_width - 230, height=800)

        ##########################down images########################
        img4 = Image.open("img4.jpg")

        img4 = img4.resize((230, 270), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=480 , width=230, height=260)

        img5 = Image.open("img5.jpg")
        img5 = img5.resize((230, 300), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=760 , width=230, height=280)

    def cust_details(self):
        self.new_window = Toplevel(self.root)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = screen_width - 230
        height = screen_height - 340   # 🔥 FIXED

        x = 230
        y = 338

        self.new_window.geometry(f"{width}x{height}+{x}+{y}")
        self.new_window.transient(self.root)

        self.app = Cust_Win(self.new_window)

    def cust_details(self):
        self.new_window = Toplevel(self.root)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = screen_width - 230
        height = screen_height - 340

        x = 230
        y = 338

        self.new_window.geometry(f"{width}x{height}+{x}+{y}")
        self.new_window.transient(self.root)

        self.app = Cust_Win(self.new_window)


    def roombooking(self):
        self.new_window = Toplevel(self.root)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = screen_width - 230
        height = screen_height - 340

        x = 230
        y = 338

        self.new_window.geometry(f"{width}x{height}+{x}+{y}")
        self.new_window.transient(self.root)

        # FIX HERE 👇
        self.app = Roombooking(self.new_window)

    




if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+230+220")
        self.root.config(bg="white")

        #Variables 
        self.var_contact = StringVar()
        self.var_checkinDate = StringVar()
        self.var_checkoutDate = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_numofdays = StringVar()
        self.var_taxpaid = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        self.var_search = StringVar()
        self.txt_search = StringVar()

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

        # Customer Contact Label
        lbl_cust_contact = Label(labelframeleft,
                                text="Customer Contact:",
                                font=("times new roman", 12, "bold"),
                                bg="white", fg="black")
        lbl_cust_contact.grid(row=0, column=0, padx=10, pady=8, sticky="w")

 
        contact_frame = Frame(labelframeleft, bg="white")
        contact_frame.grid(row=0, column=1, padx=10, pady=8, sticky="w")

        txt_cust_ref = Entry(contact_frame,
                            textvariable=self.var_contact,
                            width=15,
                            bg="white",
                            fg="black",
                            insertbackground="black",
                            relief=RIDGE,
                            bd=2)
        txt_cust_ref.pack(side=LEFT, padx=(0,5))

        btnFetchData = Button(contact_frame,
                            command=self.Fetch_contact,
                            text="Fetch",
                            font=("times new roman", 10, "bold"),
                            bg="black",
                            fg="gold",
                            width=8)

        btnFetchData.pack(side=LEFT)

        # ================= CHECK-IN DATE =================
        lblCheckIn = Label(labelframeleft, text="Check-In Date:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblCheckIn.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        txt_checkin = Entry(labelframeleft,textvariable=self.var_checkinDate, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_checkin.grid(row=1, column=1, padx=10, pady=5)


        # ================= CHECK-OUT DATE =================
        lblCheckOut = Label(labelframeleft, text="Check-Out Date:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblCheckOut.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        txt_checkout = Entry(labelframeleft,textvariable=self.var_checkoutDate, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_checkout.grid(row=2, column=1, padx=10, pady=5)


        # ================= ROOM TYPE =================
        label_RoomType = Label(labelframeleft, text="Room Type:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        label_RoomType.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=33, state="readonly")
        combo_RoomType['values'] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1, padx=10, pady=5)


        # ================= AVAILABLE ROOM =================
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblRoomAvailable.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        txt_room_available = Entry(labelframeleft,textvariable=self.var_roomavailable, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_room_available.grid(row=4, column=1, padx=10, pady=5)


        # ================= MEAL =================
        lblMeal = Label(labelframeleft, text="Meal:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblMeal.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        txt_meal = Entry(labelframeleft,textvariable=self.var_meal, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_meal.grid(row=5, column=1, padx=10, pady=5)


        # ================= NUMBER OF DAYS =================
        lblNoOfDays = Label(labelframeleft, text="Number of days:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblNoOfDays.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        txt_no_days = Entry(labelframeleft,textvariable=self.var_numofdays, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_no_days.grid(row=6, column=1, padx=10, pady=5)


        # ================= TAX PAID =================
        lblTaxPaid = Label(labelframeleft, text="Tax Paid:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblTaxPaid.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        txt_tax = Entry(labelframeleft,textvariable=self.var_taxpaid, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_tax.grid(row=7, column=1, padx=10, pady=5)


        # ================= SUB TOTAL =================
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblSubTotal.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        txt_subtotal = Entry(labelframeleft,textvariable=self.var_actualtotal, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_subtotal.grid(row=8, column=1, padx=10, pady=5)


        # ================= TOTAL COST =================
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lblTotalCost.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        txt_total = Entry(labelframeleft,textvariable=self.var_total, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        txt_total.grid(row=9, column=1, padx=10, pady=5)

        #Bill button 
        btnBill = Button(labelframeleft, text="Bill",command=self.total, font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnBill.grid(row=10,column=0,columnspan=2,padx=5, pady=(10,5), sticky="w")


        # ==================Buttons==================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE, bg="white")
        btn_frame.grid(row=11, column=0, columnspan=2, pady=10)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnDelete.grid(row=0,column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnReset.grid(row=0,column=3, padx=1)

        #RightSide Image
        img3 = Image.open("bed.jpg")
        img3 = img3.resize((550, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.photoimg3, bg="white")
        lbl_img3.place(x=760, y=55, width=550, height=250)


        # ================= table frame search system =====================
        Table_Frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="View Details & Search System",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black"
        )

        Table_Frame.place(x=440, y=280, width=850, height=260)

        # ================= SEARCH LABEL =====================
        lbl_Searchby = Label(
            Table_Frame,
            text="Search By:",
            font=("times new roman", 12, "bold"),
            bg="red",
            fg="white",
            bd=2,
            relief="solid",
            padx=6,
            pady=2

        )
        lbl_Searchby.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.search_var = StringVar()

        # ================= SEARCH COMBOBOX =====================
        combo_Search = ttk.Combobox(
            Table_Frame,
            textvariable= self.search_var,
            font=("times new roman", 12),
            width=20,
            state="readonly"
        )

        combo_Search["values"] = ("mobile", "roomtype")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=10, pady=10)

        # ================= SEARCH ENTRY =====================
        self.txt_search = StringVar()
        txt_search = Entry(
            Table_Frame,
            textvariable=self.txt_search, 
            width=25,
            font=("times new roman", 12),
            bg="white",
            fg="black",
            relief=RIDGE,
            bd=2
        )
        txt_search.grid(row=0, column=2, padx=10, pady=10)

        # ================= SEARCH BUTTON =====================
        btnSearch = Button(
            Table_Frame,
            text="Search",
            command=self.search,
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black",
            width=10
        )
        btnSearch.grid(row=0, column=3, padx=5)

        # ================= SHOW ALL BUTTON =====================
        btnShowAll = Button(
            Table_Frame,
            text="Show All",
            command=self.fetch_data,
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black",
            width=10
        )
        btnShowAll.grid(row=0, column=4, padx=5)

        # ================== TABLE FRAME ==================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE, bg="white")
        details_table.place(x=0, y=50, width=860, height=150)

        # Prevent auto resizing
        details_table.pack_propagate(False)

        # ================== SCROLLBARS ==================
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # ================== TREEVIEW ==================
        self.Cust_Details_Table = ttk.Treeview(
            details_table,
            columns=("mobile", "checkinDate", "checkoutDate", "roomtype", "roomavailable",
                    "meal", "numofdays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # ================== HEADINGS ==================
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("checkinDate", text="Check-in")
        self.Cust_Details_Table.heading("checkoutDate", text="Check-out")
        self.Cust_Details_Table.heading("roomtype", text="Room Type")
        self.Cust_Details_Table.heading("roomavailable", text="Room Num")
        self.Cust_Details_Table.heading("meal", text="Meal")
        self.Cust_Details_Table.heading("numofdays", text="Num of Days")
        
        # ================== SHOW HEADINGS ==================
        self.Cust_Details_Table["show"] = "headings"

        # ================== COLUMN WIDTH ==================
        self.Cust_Details_Table.column("mobile", width=80)
        self.Cust_Details_Table.column("checkinDate", width=120)
        self.Cust_Details_Table.column("checkoutDate", width=120)
        self.Cust_Details_Table.column("roomtype", width=80)
        self.Cust_Details_Table.column("roomavailable", width=80)
        self.Cust_Details_Table.column("meal", width=150)
        self.Cust_Details_Table.column("numofdays", width=100)
        

        # ================== PACK ORDER (IMPORTANT) ==================
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
    #add data
    def add_data(self):

            if self.var_contact.get() == "" or self.var_checkinDate.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="hoteluser",
                        password="1234",
                        database="hotel"
                    )
                    my_cursor = conn.cursor()

                    # Example insert query
                    my_cursor.execute("INSERT INTO room  VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkinDate.get(),
                                                                                        self.var_checkoutDate.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_numofdays.get()
                                                                                        
                                                                                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Room Booked", parent=self.root)

                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="hoteluser",
            password="1234",
            database="hotel"
        )

        my_cursor = conn.cursor() 

        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()

        conn.close()

        #get cursor
    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)

        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkinDate.set(row[1])
        self.var_checkoutDate.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_numofdays.set(row[6])

    #update data 

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
            return



        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="hoteluser",
                password="1234",
                database="hotel"
            )

            cursor = conn.cursor()

            query = """
            UPDATE room SET
            checkinDate=%s,
            checkoutDate=%s,
            roomtype=%s,
            roomavailable=%s,
            meal=%s,
            numofdays=%s
            WHERE mobile=%s
            """

            values = (
                
                self.var_checkinDate.get(),
                self.var_checkoutDate.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_numofdays.get(),
                self.var_contact.get(),
            )

            cursor.execute(query, values)
            conn.commit()

            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Room details has been updated successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)

    # delete function 

    def mDelete(self):

        mDelete = messagebox.askyesno(
            "Hotel Management System",
            "Do you want to delete this customer?",
            parent=self.root
        )

        if mDelete:
            conn = mysql.connector.connect(
                host="localhost",
                user="hoteluser",
                password="1234",
                database="hotel"
            )

            my_cursor = conn.cursor()

            query = "DELETE FROM room WHERE mobile=%s"
            value = (self.var_contact.get(),)

            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            conn.close()

    #reset function 

    def reset(self):
        self.var_contact.set("")
        self.var_checkinDate.set("")
        self.var_checkoutDate.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_numofdays.set("")
        self.var_taxpaid.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")



    #=========================All Data Fetch=======================
    
    def Fetch_contact(self):

        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="hoteluser",
                password="1234",
                database="hotel"
            )

            my_cursor = conn.cursor()

            query = """SELECT Name, Gender, Email, Nationality, Address 
                    FROM customer WHERE mobile=%s"""
            
            value = (self.var_contact.get(),)

            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            # 🔴 DEBUG (you can remove later)
            print("Fetched Row:", row)

            if row is None:
                messagebox.showerror("Error", "No Data Found", parent=self.root)
                return

            # ✅ Extract values properly
            name = row[0]
            gender = row[1]
            email = row[2]
            nationality = row[3]
            address = row[4]

            conn.close()

            # ✅ Clear previous data (VERY IMPORTANT)
            for widget in self.showDatarame.winfo_children():
                widget.destroy()

            # ✅ Display labels (WHITE BACKGROUND)
            Label(self.showDatarame, text="Name:", bg="white", font=("arial",12,"bold"),fg="black").place(x=0,y=0)
            Label(self.showDatarame, text=name, bg="white", font=("arial",12,"bold"),fg="black").place(x=100,y=0)

            Label(self.showDatarame, text="Gender:", bg="white", font=("arial",12,"bold"),fg="black").place(x=0,y=30)
            Label(self.showDatarame, text=gender, bg="white", font=("arial",12,"bold"),fg="black").place(x=100,y=30)

            Label(self.showDatarame, text="Email:", bg="white", font=("arial",12,"bold"),fg="black").place(x=0,y=60)
            Label(self.showDatarame, text=email, bg="white", font=("arial",12,"bold"),fg="black").place(x=100,y=60)

            Label(self.showDatarame, text="Nationality:", bg="white", font=("arial",12,"bold"),fg="black").place(x=0,y=90)
            Label(self.showDatarame, text=nationality, bg="white", font=("arial",12,"bold"),fg="black").place(x=100,y=90)

            Label(self.showDatarame, text="Address:", bg="white", font=("arial",12,"bold"),fg="black").place(x=0,y=120)
            Label(self.showDatarame, text=address, bg="white", font=("arial",12,"bold"),fg="black").place(x=100,y=120)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    #search system

    def search(self):
        if self.search_var.get() == "" or self.txt_search.get() == "":
            messagebox.showerror("Error", "Please select option and enter value")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="hoteluser",
                password="1234",
                database="hotel"
            )

            my_cursor = conn.cursor()

            query = f"SELECT * FROM room WHERE {self.search_var.get()}=%s"
            my_cursor.execute(query, (self.txt_search.get(),))

            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for row in rows:
                    self.Cust_Details_Table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No record found")

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")

    

    def total(self):

        # Convert dates
        inDate = datetime.strptime(self.var_checkinDate.get(), "%Y-%m-%d")
        outDate = datetime.strptime(self.var_checkoutDate.get(), "%Y-%m-%d")

        days = abs((outDate - inDate).days)
        self.var_numofdays.set(days)

        # Room price logic (simple + safe)
        if self.var_roomtype.get() == "Single":
            room_price = 1000
        elif self.var_roomtype.get() == "Double":
            room_price = 1500
        else:
            room_price = 2000

        # Meal price
        if self.var_meal.get().lower() == "veg":
            meal_price = 200
        else:
            meal_price = 300

        # Total calculation
        subtotal = (room_price + meal_price) * days
        tax = subtotal * 0.1
        total = subtotal + tax

        # Set values in UI
        self.var_actualtotal.set(f"{subtotal:.2f}")
        self.var_taxpaid.set(f"{tax:.2f}")
        self.var_total.set(f"{total:.2f}")
            








                




if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
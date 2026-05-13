from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Section")
        self.root.geometry("1295x550+230+220")
        self.root.config(bg="white")

        #===============variables====================
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_pin = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ================= STYLE FIX (COMBOBOX WHITE) =================
        style = ttk.Style()
        style.theme_use('default')

        style.configure(
            "TCombobox",
            fieldbackground="white",
            background="white",
            foreground="black"
        )

        style.map("TCombobox",
                  fieldbackground=[("readonly", "white")],
                  background=[("readonly", "white")])

        # ================= TITLE =================
        lbl_title = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
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

        # ================= LEFT FRAME =================
        labelframeleft = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Customer Details",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black"
        )
        labelframeleft.place(x=5, y=5, width=425, height=490)

        # ================= CUSTOMER REF =================
        lbl_ref = Label(labelframeleft, text="Customer Ref:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_ref.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        entry_ref = Entry(labelframeleft,textvariable=self.var_ref, width=25, bg="white", fg="black", relief=RIDGE, bd=2, state="readonly", readonlybackground="white")
        entry_ref.grid(row=0, column=1, padx=10, pady=5)

        # ================= NAME =================
        lbl_name = Label(labelframeleft, text="Customer Name:", font=("times new roman", 12, "bold"), bg="white",fg="black")
        lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        entry_name = Entry(labelframeleft,textvariable=self.var_cust_name ,width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_name.grid(row=1, column=1, padx=10, pady=5)

        # ================= MOTHER NAME =================
        lbl_mother = Label(labelframeleft, text="Mother's Name:", font=("times new roman", 12, "bold"), bg="white",fg="black")
        lbl_mother.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        entry_mother = Entry(labelframeleft, textvariable=self.var_mother ,width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_mother.grid(row=2, column=1, padx=10, pady=5)

        # ================= GENDER =================
        lbl_gender = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_gender.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        combo_gender = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_gender,
            font=("times new roman", 12),
            width=35,
            state="readonly"
        )
        combo_gender["values"] = ("Male", "Female", "Rather not say")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1, padx=10, pady=5)

        # ================= PIN CODE =================
        lbl_pin = Label(labelframeleft, text="Pin Code:", font=("times new roman", 12, "bold"), bg="white",fg="black")
        lbl_pin.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        entry_pin = Entry(labelframeleft, textvariable=self.var_pin,width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_pin.grid(row=4, column=1, padx=10, pady=5)

        # ================= CONTACT =================
        lbl_contact = Label(labelframeleft, text="Contact:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_contact.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        entry_contact = Entry(labelframeleft,textvariable=self.var_contact, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_contact.grid(row=5, column=1, padx=10, pady=5)

        # ================= EMAIL =================
        lbl_email = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_email.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        entry_email = Entry(labelframeleft,textvariable=self.var_email ,width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_email.grid(row=6, column=1, padx=10, pady=5)

        # ================= NATIONALITY (COMBOBOX FIX) =================
        lbl_nationality = Label(labelframeleft, text="Nationality:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_nationality.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        combo_nationality = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_nationality,
            font=("times new roman", 12),
            width=35,
            state="readonly"
        )
        combo_nationality["values"] = ("Indian", "American", "British", "Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1, padx=10, pady=5)

       
        # ================= ID PROOF =================
        lbl_Idproof = Label(
            labelframeleft,
            text="ID Proof:",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black"
        )
        lbl_Idproof.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        combo_Idproof = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_id_proof,
            font=("times new roman", 12),
            width=35,
            state="readonly"
        )

        combo_Idproof["values"] = ("Aadhaar Card", "Driver's Licence", "Passport", "Other")
        combo_Idproof.current(0)

        combo_Idproof.grid(row=8, column=1, padx=10, pady=5)

        # ================= ID NUMBER =================
        lbl_idnum = Label(labelframeleft, text="ID Number:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_idnum.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        entry_idnum = Entry(labelframeleft,textvariable=self.var_id_number, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_idnum.grid(row=9, column=1, padx=10, pady=5)

        # ================= ADDRESS =================
        lbl_address = Label(labelframeleft, text="Address:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_address.grid(row=10, column=0, padx=10, pady=5, sticky="w")

        entry_address = Entry(labelframeleft,textvariable=self.var_address, width=25, bg="white", fg="black", relief=RIDGE, bd=2)
        entry_address.grid(row=10, column=1, padx=10, pady=5)

        # ==================Buttons==================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnAdd.grid(row=0,column=0, padx=1)


        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnDelete.grid(row=0,column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("times new roman", 12, "bold"),bg="black", fg="gold", width=10)
        btnReset.grid(row=0,column=3, padx=1)

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

        Table_Frame.place(x=440, y=5, width=850, height=490)

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

        combo_Search["values"] = ("Mobile", "Ref", "Name")
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
            width=10,
        )
        btnShowAll.grid(row=0, column=4, padx=5)

        # ================== TABLE FRAME ==================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE, bg="white")
        details_table.place(x=0, y=50, width=860, height=350)

        # Prevent auto resizing
        details_table.pack_propagate(False)

        # ================== SCROLLBARS ==================
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # ================== TREEVIEW ==================
        self.Cust_Details_Table = ttk.Treeview(
            details_table,
            columns=("ref", "Name", "Mother", "Gender", "Pin",
                    "Mobile", "Email", "nationality", "Idproof", "Idnumber", "Address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # ================== HEADINGS ==================
        self.Cust_Details_Table.heading("ref", text="Ref")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Mother", text="Mother")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("Pin", text="Pin")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("Idproof", text="ID Proof")
        self.Cust_Details_Table.heading("Idnumber", text="ID Number")
        self.Cust_Details_Table.heading("Address", text="Address")

        # ================== SHOW HEADINGS ==================
        self.Cust_Details_Table["show"] = "headings"

        # ================== COLUMN WIDTH ==================
        self.Cust_Details_Table.column("ref", width=80)
        self.Cust_Details_Table.column("Name", width=120)
        self.Cust_Details_Table.column("Mother", width=120)
        self.Cust_Details_Table.column("Gender", width=80)
        self.Cust_Details_Table.column("Pin", width=80)
        self.Cust_Details_Table.column("Mobile", width=120)
        self.Cust_Details_Table.column("Email", width=150)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("Idproof", width=120)
        self.Cust_Details_Table.column("Idnumber", width=120)
        self.Cust_Details_Table.column("Address", width=200)

        # ================== PACK ORDER (IMPORTANT) ==================
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # ================== CONNECT SCROLLBARS ==================
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

    def add_data(self):

        if self.var_contact.get() == "" or self.var_mother.get() == "":
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
                my_cursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_pin.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="hoteluser",
            password="1234",
            database="hotel"
        )

        my_cursor = conn.cursor() 

        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()

        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)

        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_pin.set(row[4])
        self.var_contact.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
            return

        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Please select a record", parent=self.root)
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
            UPDATE customer SET 
                Name=%s,
                Mother=%s,
                Gender=%s,
                Pin=%s,
                Mobile=%s,
                Email=%s,
                Nationality=%s,
                Idproof=%s,
                Idnumber=%s,
                Address=%s
            WHERE Ref=%s
            """

            values = (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_pin.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            )

            cursor.execute(query, values)
            conn.commit()

            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Customer updated successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)

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

            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.var_ref.get(),)

            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            conn.close()
            

            messagebox.showinfo("Delete", "Customer deleted successfully", parent=self.root)

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_pin.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""),
        
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="hoteluser",
            password="1234",
            database="hotel"
        )
        my_cursor = conn.cursor()

        query = "SELECT * FROM customer WHERE {} LIKE %s".format(self.search_var.get())
        value = "%" + self.txt_search.get() + "%"

        my_cursor.execute(query, (value,))
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()

        conn.close()

        
                 
             




   




         


# ================= RUN =================
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
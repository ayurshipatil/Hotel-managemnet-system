import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from hotel import HotelManagementSystem
import mysql.connector


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


# ================= LOGIN WINDOW =================
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")

        # BACKGROUND IMAGE (UNCHANGED)
        img = Image.open("/Users/ayurshipatil/code/login_form/hotel2.jpg")
        img = img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # ICON
        img1 = Image.open("/Users/ayurshipatil/code/login_form/user.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimage1, bg="black")
        lblimg1.place(x=730, y=175, width=100, height=100)

        # TITLE
        Label(frame, text="Get Started",
              font=("times new roman", 20, "bold"),
              fg="white", bg="black").place(x=100, y=110)

        # USERNAME
        Label(frame, text="Email",
              font=("times new roman", 15, "bold"),
              fg="white", bg="black").place(x=70, y=155)

        self.txtuser = Entry(frame, bg="white", fg="black", insertbackground="black")
        self.txtuser.place(x=40, y=180, width=270)

        # PASSWORD
        Label(frame, text="Password",
              font=("times new roman", 15, "bold"),
              fg="white", bg="black").place(x=70, y=225)

        self.txtpass = Entry(frame, bg="white", fg="black", insertbackground="black", show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # LOGIN BUTTON
        Button(frame, text="Login",
               font=("times new roman", 15, "bold"),
               bg="white", fg="black",
               command=self.login).place(x=110, y=300, width=120)

        # REGISTER BUTTON
        Button(frame, text="New User Register",
               command=self.register_window,
               font=("times new roman", 12),
               fg="white", bg="black", bd=0).place(x=90, y=350)

        # FORGOT PASSWORD
        Button(frame, text="Forgot Password?",
               command=self.forgot_password_window,
               font=("times new roman", 12),
               fg="white", bg="black", bd=0).place(x=90, y=380)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql123",
                database="login_system"
            )

            cur = conn.cursor()

            # Check user credentials
            cur.execute(
                "SELECT * FROM register WHERE email=%s AND password=%s",
                (self.txtuser.get().strip(), self.txtpass.get().strip())
            )

            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password")
            else:
                messagebox.showinfo("Success", "Login Successful")

                # Close login window
                self.root.destroy()

                # Open main hotel dashboard
                from hotel import HotelManagementSystem

                root = Tk()
                app = HotelManagementSystem(root)
                root.mainloop()

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"{str(es)}")

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter your email to reset password")
            return
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="mysql123",
                    database="login_system"
            )
            cur = conn.cursor()
            query=("select * from register where email=%s ")
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            #print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter valid username")
            else:
                messagebox.showinfo("success","Email found! You can reset your password")


                #-----------RESET WINDIOOW---------------#
                self.reset_window = Toplevel(self.root)
                self.reset_window.title("Reset Password")
                self.reset_window.geometry("400x300+600+200")

                Label(self.reset_window, text="New Password", font=("times new roman", 12)).place(x=50, y=50)
                self.new_pass = Entry(self.reset_window, show="*", font=("times new roman", 12))
                self.new_pass.place(x=180, y=50, width=150)

                Label(self.reset_window, text="Confirm Password", font=("times new roman", 12)).place(x=50, y=100)
                self.conf_pass = Entry(self.reset_window, show="*", font=("times new roman", 12))
                self.conf_pass.place(x=180, y=100, width=150)

                Button(self.reset_window, text="Reset", command=self.reset_password,
                       bg="green", fg="white").place(x=150, y=160, width=100)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"{str(es)}")

                
      

        #------------RESET PASSWORD fUNCTION---------------------#
    def reset_password(self):

        if self.new_pass.get() == "" or self.conf_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        if self.new_pass.get() != self.conf_pass.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql123",
                database="login_system"
            )

            cur = conn.cursor()

            cur.execute(
                "UPDATE register SET password=%s WHERE email=%s",
                (self.new_pass.get(), self.txtuser.get())
            )

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Password reset successfully")
            self.reset_window.destroy()

        except Exception as es:
            messagebox.showerror("Error", f"{str(es)}")
        
            
# ================= REGISTER WINDOW =================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # BACKGROUND IMAGE (UNCHANGED)
        self.bg = ImageTk.PhotoImage(
            file="/Users/ayurshipatil/code/login_form/registerimgbg.png"
        )
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        Label(frame, text="REGISTER HERE",
              font=("times new roman", 20, "bold"),
              bg="white", fg="green").place(x=50, y=30)

        # VARIABLES
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # ===== FIXED FIELDS =====

        Label(frame, text="First Name", bg="white", fg="black").place(x=50, y=100)
        Entry(frame, textvariable=self.var_fname,
              bg="white", fg="black", insertbackground="black").place(x=50, y=130, width=250)

        Label(frame, text="Last Name", bg="white", fg="black").place(x=370, y=100)
        Entry(frame, textvariable=self.var_lname,
              bg="white", fg="black", insertbackground="black").place(x=370, y=130, width=250)

        Label(frame, text="Contact No", bg="white", fg="black").place(x=50, y=180)
        Entry(frame, textvariable=self.var_contact,
              bg="white", fg="black", insertbackground="black").place(x=50, y=210, width=250)

        Label(frame, text="Email", bg="white", fg="black").place(x=370, y=180)
        Entry(frame, textvariable=self.var_email,
              bg="white", fg="black", insertbackground="black").place(x=370, y=210, width=250)

        Label(frame, text="Security Question", bg="white", fg="black").place(x=50, y=260)

        combo = ttk.Combobox(frame, textvariable=self.var_securityQ, state="readonly")
        combo["values"] = ("Your Birth Place", "Your Pet Name", "Your School Name")
        combo.place(x=50, y=290, width=250)

        Label(frame, text="Answer", bg="white", fg="black").place(x=370, y=260)
        Entry(frame, textvariable=self.var_securityA,
              bg="white", fg="black", insertbackground="black").place(x=370, y=290, width=250)

        Label(frame, text="Password", bg="white", fg="black").place(x=50, y=340)
        Entry(frame, textvariable=self.var_pass,
              bg="white", fg="black", insertbackground="black", show="*").place(x=50, y=370, width=250)

        # Confirm Password
        Label(frame, text="Confirm Password", bg="white", fg="black",
              font=("times new roman", 12)).place(x=370, y=340)

        Entry(frame, textvariable=self.var_confpass,
              bg="white", fg="black", insertbackground="black", show="*").place(x=370, y=370, width=250)

        # REGISTER BUTTON IMAGE
        img = Image.open("/Users/ayurshipatil/code/login_form/registerbtn.png")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        Button(frame, image=self.photo,
               command=self.register_data,
               borderwidth=0, cursor="hand2").place(x=300, y=440)

    def register_data(self):
        if self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match")
            return
    
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql123",
                database="login_system"
            )
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                )
            )

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registered Successfully")

        except Exception as es:
            messagebox.showerror("Error", f"{str(es)}")


if __name__ == "__main__":
    main()
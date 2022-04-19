from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import pickle 

root = Tk()
root.geometry("600x800")
root.resizable(False, False)
root["bg"] = "#FFF"
root.title("New? Create an account")

def registration():
    text_str1 = Label(text="Welcome to Thinkz! ")
    text_str2 = Label(text="We happy to make your city smarter! ")
    text_str3 = Label(text="Please complete the following profile mandatory fileds: ")
    text_Video = Label(text="Get started by see this explanation video:")
    button_video = Button(text="Video")
    text_presentation1 = Label(text="Use Thinkz platform to manage your smart city and give an advantage and ")
    text_presentation2 = Label(text="information to the tourists, residents to city stack-holders")
    text_Fn = Label(text="First name")
    regisrt_firstname = Entry()
    text_Ln = Label(text="Last name")
    regisrt_lastname = Entry()
    text_City = Label(text="City name")
    regisrt_city = Entry()
    text_Country = Label(text="Country")
    button_country = Button(text="Choose")
    text_Role = Label(text="Role")
    button_role = Button(text="Choose")
    text_Email = Label(text="Email")
    regisrt_email = Entry()
    text_Password = Label(text="Password")
    regisrt_password = Entry(show="*")
    button_policy1 = Button ()
    button_policy2 = Button(text="Privacy policy")
    button_getstarted = Button(text="Get started", command=lambda: save())
    button_contact = Button(text="Any questions?Contact us")
    

    text_str1.place(x=100, y=20)
    text_str2.place(x=50, y=60)
    text_str3.place(x=30, y=170)
    text_Video.place(x=150, y=210)
    button_video.place(x=170, y=240, width=180, height=50)
    text_presentation1.place(x=85, y=300)
    text_presentation2.place(x=130, y=320)
    text_Fn.place(x=170, y=360) 
    regisrt_firstname.place(x=250, y=360, width=150, height=18)
    text_Ln.place(x=170, y=400)
    regisrt_lastname.place(x=250, y=400, width=150, height=18)
    text_City.place(x=170, y=440)
    regisrt_city.place(x=250, y=440, width=150, height=18)
    text_Country.place(x=175, y=480)
    button_country.place(x=250, y=480, width=140, height=30)
    text_Role.place(x=185, y=520)
    button_role.place(x=250, y=515, width=140, height=30)
    text_Email.place(x=180, y=560)
    regisrt_email.place(x=250, y=560, width=150, height=18)
    text_Password.place(x=167, y=600)
    regisrt_password.place(x=250, y=600, width=150, height=18)
    button_policy1.place(x=250, y=640, width=18, height=18)
    button_policy2.place(x=275, y=635)
    button_getstarted.place(x=200, y=690, width=210, height=35)
    button_contact.place(x=2, y=770)
        

    def save():
        login_pass_save = {}
        login_pass_save[regisrt_firstname.get()]=regisrt_password.get()
        login_pass_save[regisrt_lastname.get()]=regisrt_password.get()
        login_pass_save[regisrt_city.get()]=regisrt_password.get()
        login_pass_save[regisrt_email.get()]=regisrt_password.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()
        
def start_window ():
        new_window = Toplelevel(tk)
        new_window.title("Login ")
        new_window.resizable(0, 0)
        canvas = Canvas(new_window, width=200, height=200)
        canvas.pack()
        
            

def login():
    text_enter_username =Label(text="User name:")
    enter_username = Entry()
    text_enter_password = Label(text="Password:")
    enter_password = Entry(show="*")
    button_signin = Button(text="Keep me sign in")
    button_forgotpass = Button(text="Forgot password?(link)")
    button_enter = Button(text="Log in", command=lambda: log_pass() )
    button_new = Button(text="New? Create an account")
    button_privacy = Button(text="privacy")

    text_enter_username.pack() 
    enter_username.pack() 
    text_enter_password.pack() 
    enter_password.pack() 
    button_signin.pack() 
    button_forgotpass.pack() 
    button_enter.pack() 
    button_new.pack() 
    button_privacy.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_username.get()]:
               messagebox.showinfo("Success")
            else:
               messagebox.showerror("wrong login or password")
        else:
            massagebox.showerror("wrong login")

            

registration ()




root.mainloop()

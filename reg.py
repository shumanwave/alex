from tkinter import *
from tkinter import messagebox
import pickle 

root = Tk()
root.geometry("500x500")
root.title("New? Create an account")

def registration():
    text_Video = Label(text="Get started by see this explanation video:")
    button_video = Button(text="Video")
    text_presentation = Label(text="Use Thinkz to manage your smart city and give an advantage and information to the tourists, residents to city stack-holders")
    text_Fn = Label(text="First Name")
    regisrt_firstname = Entry()
    text_Ln = Label(text="Last Name")
    regisrt_lastname = Entry()
    text_City = Label(text="City Name")
    regisrt_city = Entry()
    text_Country = Label(text="Country")
    regisrt_country = Entry()
    text_Role = Label(text="Role")
    regisrt_role = Entry()
    text_Email = Label(text="Email")
    regisrt_email = Entry()
    text_Password = Label(text="Password")
    regisrt_password = Entry(show="*")
    button_policy = Button(text="Privacy policy")
    button_getstarted = Button(text="Get started", command=lambda: save())
    button_contact = Button(text="Any questions?Contact us")

    text_Video.pack()
    button_video.pack()
    text_presentation.pack()
    text_Fn.pack() 
    regisrt_firstname.pack()
    text_Ln.pack()
    regisrt_lastname.pack()
    text_City.pack()
    regisrt_city.pack()
    text_Country.pack()
    regisrt_country.pack()
    text_Role.pack()
    regisrt_role.pack()
    text_Email.pack()
    regisrt_email.pack()
    text_Password.pack()
    regisrt_password.pack()
    button_policy.pack()
    button_getstarted.pack()
    button_contact.pack()
    button_video.pack()

    def save():
        login_pass_save = {}
        login_pass_save[regisrt_firstname.get()]=regisrt_password.get()
        login_pass_save[regisrt_lastname.get()]=regisrt_password.get()
        login_pass_save[regisrt_city.get()]=regisrt_password.get()
        login_pass_save[regisrt_country.get()]=regisrt_password.get()
        login_pass_save[regisrt_role.get()]=regisrt_password.get()
        login_pass_save[regisrt_email.get()]=regisrt_password.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()
        

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
    

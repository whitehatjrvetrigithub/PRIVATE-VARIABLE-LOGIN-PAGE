from tkinter import *
root = Tk()

root.title("Private Variable Login Page")
root.geometry("600x600")

name_lbl = Label(root, text = "Name :")
name_lbl.place(relx = 0.4, rely = 0.1, anchor = CENTER)

name_entry = Entry(root)
name_entry.place(relx = 0.6, rely = 0.1, anchor = CENTER)

pw_lbl = Label(root, text = "Password :")
pw_lbl.place(relx = 0.4, rely = 0.2, anchor = CENTER)

pw_entry = Entry(root)
pw_entry.place(relx = 0.6, rely = 0.2, anchor = CENTER)

captcha_lbl = Label(root, text = "Captcha :")
captcha_lbl.place(relx = 0.4, rely = 0.3, anchor = CENTER)

captcha_entry = Entry(root)
captcha_entry.place(relx = 0.6, rely = 0.3, anchor = CENTER)

updated_name_lbl = Label(root)
updated_name_lbl.place(relx = 0.5, rely = 0.7, anchor = CENTER)

updated_pw_lbl = Label(root)
updated_pw_lbl.place(relx = 0.5, rely = 0.8, anchor = CENTER)

updated_captcha_lbl = Label(root)
updated_captcha_lbl.place(relx = 0.5, rely = 0.9, anchor = CENTER)

class userDB():
    
    def __init__(self):
        self.__username = "Vetri"
        self.__password = "41918_285_36457"
        self.captcha = captcha_entry.get()
        
    def showUser(self):
        updated_name_lbl["text"] = "Name : " + self.__username
        updated_pw_lbl["text"] = "Password : " + self.__password
        updated_captcha_lbl["text"] = "Captcha : " + self.captcha
        

user = userDB()

def addUser():
    global user 
    user.username = name_entry.get()
    user.password = pw_entry.get()
    user.captcha = captcha_entry.get()
    
add_btn = Button(root, text = "Update Login Details", command = addUser)
add_btn.place(relx = 0.4, rely = 0.5, anchor = CENTER)

show_btn = Button(root, text = "Show Profile", command = user.showUser)
show_btn.place(relx = 0.6, rely = 0.5, anchor = CENTER)

root.mainloop()
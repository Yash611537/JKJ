from tkinter import *

def submitact():
    if username.get() == "Yash_Shah" and password.get() == "yash12140":
        print("Login Successful")
    else:
        print("Login failed")


window = Tk()
window.geometry("400x150")

l1 = Label(window, text="Enter username: ")
l1.place(x=50, y=20)

username = Entry(window, width=50)
username.place(x=150, y=20)

l2 = Label(window, text="Enter password: ")
l2.place(x=50, y=50)

password = Entry(window, show="*", width=50)
password.place(x=150, y=50)

submit = Button(window, text="Login", command=submitact)
submit.place(x=150, y=85)

window.mainloop()
import tkinter
from email.message import Message
from tkinter import messagebox as msg
from beauty_salon.manage_employee import *



class EmployeeWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("مدیریت کارمندان")
        self.window.geometry("400*300")


        #ورودی ها
        self.label_name = tkinter.label(window, text="نام کارمند:")
        self.label_name.pack(pady=5)
        self.entry_name = tkinter.Entry(window)
        self.entry_name.pack(pady=5)

        self.label_phone = tkinter.Label(window, text="شماره تلفن:")
        self.label_phone.pack(pady=5)
        self.entry_phone = tkinter.Entry(window)
        self.entry_phone.pack(pady=5)

      #دکمه های اضافه کردن
        self.btn_add = tkinter.Button(window, text="اضافه کردن کارمندان", command=self.add_employee)
        self.btn_add.pack(pady=10)


        #لیست کارمندان
        self.listbox = tkinter.Listbox(window)
        self.listbox.pack(pady=10, fill=tkinter.BOTH, expand=True)

    def add_employee(self):
        name = self.entry_name.get()
        photo = self.entry_phone.get()
        if name and photo:
            self.listbox.insert(tkinter.END, f"{name} - {photo}")
            self.entry_name.delete(0, tkinter.END)
            self.entry_phone.delete(0, tkinter.END)
        else:

           msg.showwarning("خطا!!! لطفا نام و شماره تلفن را وارد کنید")
   # if __name__ == "--main__":
    #   root = tkinter.Tk
    #app = MainApp(root)
     #  root.mainloop()

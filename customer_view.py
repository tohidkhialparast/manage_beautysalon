from tkinter import Tk
from tkinter import messagebox
from beauty_salon.manage_employee import *



class CustomerWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("مدیریت مشتریان")
        self.window.geometry("400x300")

#لیست مشتریان(مدل)
        self.customers = []

#ویو
        self.label_name = Tk.Label(window, text="نام مشتری :")
        self.label_name.pack(pady=5)
        self.entry_name = Tk.Entry(window)

        self.label_phone = Tk.Label(window, text="شماره مشتری :")
        self.entry_phone = Tk.Entry(window)
        self.label_phone.pack(pady=5)


        self.btn_add = Tk.Button(window, text="اضافه کردن مشتری :", command=self.add_customer)
        self.btn_add.pack(pady=10)
        self.Listbox = Tk.Listbox(window)
        self.Listbox.pack(pady=10, fill=Tk.BOTH, expand=True)



    def aad_customer(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name and phone :
            customer_id = len(self.customers) + 1
            customer = Customer(customer_id, name, phone)


#نمایش در ویو
        self.Listbox.insert(tk.END.str(customer))


#پاک کردن فیلد های ورودی


         self.entry_name.delete(0,Tk.END)
         self.entry_phone.delete(0, Tk.END)
        else:
messagebox.showwarning("خطا لطفا نام و شماره تلفن را وارد کنید ")

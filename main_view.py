import tkinter as tk
from tkinter import messagebox
from beauty_salon.manage_employee import *

from beauty_salon.manage_employee import Customer, Service


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("سالن زیبایی")
        self.root.geometry("300*200")


        # دکمه ها
        self.btn_employee= tk.Button(root, text="مدیریت کارمندان", command=self.open_employee_window)
        self.btn_employee.pack(pady=10)

        self.btn_customers = tk.Button(root, text="مدیریت مشتریان", command=self.open_customer_window)
        self.btn_customers.pack(pady=10)

        self.btn_services = tk.Button(root, text="مدیریت خدمات", command=self.open_services_window)
        self.btn_services.pack(pady=10)

    def open_employee_window(self):
        employee_window = tk.Toplevel(self.root)EmployeeWindow(employee_window)

    def open_customer_window(self):
        customer_window = tk.Toplevel(self.root)CustomerWindow(customer_window)
        
    def open_service_window(self):
        Service_window=tk.Toplevel(self.root)ServiceWindow(Service_window)


MainApp.mainlop()

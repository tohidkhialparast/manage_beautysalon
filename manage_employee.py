import self
import _tkinter as tk
from tkinter import messagebox


class Employee:
    def __init__(self, employee_id, name, phone):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.salary = 0 #حقوق کارمند
    def add_salary(self,amount):
        self.salary+= amount
    def __str__(self):
        return f"Employee_ID:{self.employee_id},name:{self.name}, phone: {self.phone}, salary:{self.salary}"

class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"Customer ID:{self.customer_id}, name = {self.name}, phone= {self.phone}"


class Service:
    def __init__(self, service_id, name, price):
        self.service_id = service_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Service ID:{self.service_id}, name:{self.name}, price: {self.price}تومان"


class Payment:
    def __init__(self, payment_id, employee, amount):
        self.payment_id= payment_id
        self.employee = employee
        self.amount = amount

    def __str__(self):
        return f"Payment_id:{self.payment_id}, Employee:{self.employee.name},Amount:{self.amount} "


class Appointment:
    def __init__(self, appointment_id, employee, customer, service,):
        self.appointment_id = appointment_id
        self.employee = employee
        self.customer= customer
        self.service= service
    def __str__(self):
        return  f"appointment_id:{self.appointment_id}, Employee:{self.employee.name},customer:{self.customer.name},service:{self.service.name} "

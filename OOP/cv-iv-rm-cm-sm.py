class Employee:

    num_of_emps=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@gmail.com'
        self.pay=pay
        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay=self.pay*self.raise_amt
        return self.pay
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
    
    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            print('Holiday')
        else:
            print('workday')

        

emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Tim','Gordon',60000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.apply_raise())
print(Employee.num_of_emps)

emp_str='John-Doe-70000'
emp_3=Employee.from_string(emp_str)
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_3.email)
print(Employee.num_of_emps)

import datetime
mydate=datetime.date(2021,2,22)
Employee.is_workday(mydate)
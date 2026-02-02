class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_wage, hours_worked):
        super().__init__(fname, lname)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_paycheck(self):
        return self.hourly_wage * self.hours_worked
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_amount, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_amount * self.commission_rate
        return regular_salary + total_commission
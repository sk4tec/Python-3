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
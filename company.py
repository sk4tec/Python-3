from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        for emp in self.employees:
            print(f"{emp.fname} {emp.lname}")
        print('-----------------------------')
    
    def pay_employees(self):
        for emp in self.employees:
            paycheck = emp.calculate_paycheck()
            print(f"Paying {emp.fname} {emp.lname} an amount of: ${paycheck:.2f}")

def main():
    testCompany = Company("TechCorp")
    emp1 = SalaryEmployee("Sarah", "Hess", 50000)
    emp2 = HourlyEmployee("Lee", "Smith", 25, 50)
    emp3 = ComissionEmployee("Bob", "Brown", 30000, 5, 200)

    testCompany.add_employee(emp1)
    testCompany.add_employee(emp2)
    testCompany.add_employee(emp3)

    testCompany.display_employees()
    testCompany.pay_employees()

    print(f"Paycheck for {emp2.fname} {emp2.lname}: ${emp2.calculate_paycheck():.2f}")

if __name__ == "__main__": # ensures this runs only when executed directly, not when imported, look at classes/person.py    
    main()
from person import Person

class Company:
    def __init__(self, name, employees=None):
        self.name = name
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, person):
        if isinstance(person, Person):
            self.employees.append(person)
        else:
            raise ValueError("Only Person instances can be added as employees.")

    def list_employees(self):
        return [employee.greet() for employee in self.employees]
    
def main():
    company = Company("TechCorp")
    emp1 = Person("Alice", 28)
    emp2 = Person("Bob", 34)

    company.add_employee(emp1)
    company.add_employee(emp2)

    for greeting in company.list_employees():
        print(greeting)

if __name__ == "__main__":  # ensures this runs only when executed directly, not when imported
    main()
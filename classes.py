class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

#main program
# Creating an instance of the person class
person = person("SunjBob", 30)
print(person.greet())

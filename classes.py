class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

def main():
    p = person("SunjBob", 30)
    print(p.greet())


if __name__ == "__main__":
    main()
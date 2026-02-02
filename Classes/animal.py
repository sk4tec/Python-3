class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping."

    def speak(self):
        return f"{self.name} makes a sound."
    
    def name_animal(self):
        return self.name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Woof!"
    
def main():
    dog = Dog("Buddy")
    
    print(f"my name is {dog.name_animal()}")
    print(dog.speak())
    print(dog.sleep())

if __name__ == "__main__":  # ensures this runs only when executed directly, not when imported
    main()
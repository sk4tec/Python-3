class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping."

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
def main():
    dog = Dog("Buddy")
    
    print(dog.speak())
    print(dog.sleep())

if __name__ == "__main__":  # ensures this runs only when executed directly, not when imported
    main()
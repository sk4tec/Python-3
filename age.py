age = input("Enter your age: ")
age = int(age)

decades = (int(age / 10))
years = age % 10
print("You have lived for", decades, "decades and", years, "years.")
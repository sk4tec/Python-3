age = input("Enter your age: ")
age = int(age)

decades = (int(age / 10)) # convert to integer to remove decimal places
decades = age // 10       # integer division to remove decimal places

years = age % 10
print("You have lived for", decades, "decades and", years, "years.")
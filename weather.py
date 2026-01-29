temperature = int(input("Enter the temperature in Celsius: "))

if temperature > 26:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 15:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("The weather is just right!")
    print("Enjoy the outdoors!")
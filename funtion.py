def greeting(name):
    return f"Hello, {name}!"

# main program - this is the first thing that runs that is not a function
# order of funcs matters in Python
input_name = input("Enter your name: ")

print(greeting(input_name))
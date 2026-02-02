acronyms = ["API", "HTTP", "CPU", "RAM"]

try:
    definition = acronyms["CPU"]
except:
    print("Error: Only strings are allowed in the acronyms list.")
finally:
    print("The acronyms list contains:", acronyms)
print("The program continues...")
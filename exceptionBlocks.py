acronyms = ["API", "HTTP", "CPU", "RAM"]

try:
    definition = acronyms["CPU"]
except:
    print("Exception: String was not foundin the acronyms list.")
finally:
    print("The acronyms list contains:", acronyms)
print("The program continues...")
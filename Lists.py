acronym = ['LOL', 'BRB', 'IDK', 'SMH', 'TBH']
word = input("Enter a word: ").upper()

if word in acronym:
    print(f"{word} is an acronym!")
else:
    print(f"{word} is not an acronym.")
acronyms = {}

acronyms['LOL'] = 'laugh out loud'
acronyms['BRB'] = 'be right back'
acronyms['IDK'] = 'I don\'t know'

print(acronyms)

acronyms['BRB'] = 'I\'ll be back!'

print(acronyms)

del acronyms['BRB']

print(acronyms)

isItThere = acronyms.get('BRB')

print("Is 'BRB' in the dictionary?", isItThere)
print("Is 'BRB' in the dictionary?", isItThere is not None)
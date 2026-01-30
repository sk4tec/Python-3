contacts = {
    'number': 4,
    'students': [
        {'name': 'Sarah', 'age': 20, 'email': 'sarah@example.com'},
        {'name': 'John', 'age': 22, 'email': 'john@example.com'},
        {'name': 'Emily', 'age': 19, 'email': 'emily@example.com'},
        {'name': 'Michael', 'age': 21, 'email': 'michael@example.com'}
    ]
}

print("Email addresses of all students:")

for student in contacts['students']:
    print(f"student email: {student['email']}.")
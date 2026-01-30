names = ['Sarah', 'John', 'Emma', 'Michael']

for name in names:
    print(f"Hello, {name}!")

for range_item in range(0, len(names), 1):
    print(f"This is loop number {range_item} names {names[range_item]}")

# lists are zero indexed as usual
# range() treats the stop value as exclusive — it generates values up to but not including that number.
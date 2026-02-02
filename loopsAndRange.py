names = ['Sarah', 'John', 'Emma', 'Michael']

for name in names:
    print(f"Hello, {name}!")

for range_item in range(0, len(names), 1):
    print(f"This is loop number {range_item} names {names[range_item]}")

# lists are zero indexed as usual
# With range(0, len(names)), you get 0,1,2,3 — all safe indices.
# If you manually tried for i in range(0, 5) on a 4-item list, names[4] would crash.
# That's why looping over range(len(list)) is the safe, idiomatic way to iterate by index in Python.
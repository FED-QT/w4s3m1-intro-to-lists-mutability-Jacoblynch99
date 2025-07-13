# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: Upper‑case each name and store in new list
upper_names = []
for n in names:
    upper_names.append(n.capitalize())  # Or use n.upper() for all caps

# Task B: Use enumerate to print index + 1 alongside name
# Expected output:
# 1. Alice
# 2. Bob
# ...
for idx, name in enumerate(upper_names, start=1):
    print(f"{idx}. {name}")

# Task C: Demonstrate at least two list methods (e.g., insert, pop, remove, sort)
#   1. Insert a new name at position 2
upper_names.insert(1, "Eve")
print("After insert:", upper_names)
#   2. Remove "charlie"
upper_names.remove("Charlie")
print("After remove:", upper_names)
#   3. Sort the list
upper_names.sort()
print("After sort:", upper_names)
# Print the list after each operation.

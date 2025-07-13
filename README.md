# W4S3M1: In Class Activity

## 🕒 Activity Overview (15–20 min)

**Objective:**

1. Observ6e and reason about mutable vs. immutable objects via `id()`
2. Practice iterating over lists, using `for` loops, `enumerate`, and common list methods

## Part 1: Mutability vs. Immutability (≈7 min)

1. **Starter snippet (in `exercise.py`):**

   ```python
   # Part 1: Mutable vs Immutable
   a = 100
   b = a
   print("Before:", a, b, id(a), id(b))
   # Observation: "a" and "b" will have the same id value, due to "a" being intialized in memory and "b" is just a reference to "a", and is not taking any space in memory

   a += 1
   print("After a += 1:", a, b, id(a), id(b))
   # Observation: "a" will have a new id because int is an immutable value and when it is changed the memory id wil change, be will have the old id value

   x = [1, 2, 3]
   y = x
   print("Before:", x, y, id(x), id(y))
   # Observation: x and y will have the same id values, due to "x" being intialized in memory and "y" is just a reference to "x", and is not taking any space in memory


   x.append(4)
   print("After x.append(4):", x, y, id(x), id(y))
   # Observation: x and y will have the same id values, lists are mutable and don't change id value when the value is updated.
   ```

2. **Tasks:**

   - **Predict**: What will the `id` values tell us for `a` vs. `b`, and for `x` vs. `y`?
   - **Run** the code and **verify** your predictions.
   - **Answer** in comments:

     - Why did `id(a)` change but `id(x)` did not?
     - What does this say about integers vs. lists in Python?

3. **Deliverable:**

   - Add a short comment under each block explaining your observations.

---

## Part 2: Lists, `for`‑loops, `enumerate`, and Methods (≈10 min)

1. **Extend `exercise.py` with:**

   ```python
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
   ```

2. **Tasks:**

   - **Fill in** Task A to build `upper_names`.
   - **Implement** Task B using `enumerate`.
   - **Choose** and apply two list methods in Task C; print after each.
   - **Discuss**: What’s the difference between modifying `names` vs. creating a new list?

3. **Deliverable:**

   - Completed code in `exercise.py` with printed output demonstrating each step.

---

## Wrap‑Up & Discussion (≈3 min)

- **Compare**: What patterns did you notice about mutability?
- **Reflect**: When might you prefer immutability? When is a list’s mutability useful?
- **Share** one new thing you learned with the class.

Discuss your observations with your partner and be ready to share!

students = [
{"name": "Ali", "marks": 78},
{"name": "Zara", "marks": 92},
{"name": "Bilal", "marks": 65},
{"name": "Sana", "marks": 88},
]
# key tells sorted() what to sort BY - here, each student's
# "marks" value. sorted() never changes the original list,
# it returns a brand new sorted one.
sorted_by_marks = sorted(students, key=lambda student: student["marks"])
print("Ascending (lowest marks first):")
for s in sorted_by_marks:
    print(s["name"], "-", s["marks"])
# add reverse=True to sort highest marks first
top_first = sorted(students, key=lambda student: student["marks"], reverse=True)
print("\nDescending (highest marks first):")
for s in top_first:
    print(s["name"], "-", s["marks"])
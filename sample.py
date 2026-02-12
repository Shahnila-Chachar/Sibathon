import numpy as np

students = {
    "Ali": [78, 85, 90],
    "Sara": [88, 92, 80],
    "Ahmed": [60, 55, 70],
    "Ayesha": [95, 90, 93]
}

averages = {}

for name, marks in students.items():
    avg = np.mean(marks)
    averages[name] = avg

top_student = max(averages, key=averages.get)
low_student = min(averages, key=averages.get)

pass_students = []
fail_students = []

for name, avg in averages.items():
    if avg >= 60:
        pass_students.append(name)
    else:
        fail_students.append(name)

print("Student Averages:")
for name, avg in averages.items():
    print(name, ":", round(avg, 2))

print("\nTop Performer:", top_student)
print("Lowest Performer:", low_student)

print("\nPassed Students:", pass_students)
print("Failed Students:", fail_students)
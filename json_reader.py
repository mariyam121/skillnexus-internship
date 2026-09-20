import json

with open("students.json", "r") as file:
    data = json.load(file)

print("===== STUDENT DATA =====")

for student in data:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("---------------------")
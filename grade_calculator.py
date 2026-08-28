# Student Grade Calculator

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"


print("Student Grade Calculator")

number_of_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(number_of_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / number_of_subjects
grade = calculate_grade(average)

print("\n--- Student Result ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)2
marks = float(input("Enter course marks (0 - 100): "))

if 90 <= marks <= 100:
    grade, gpa = "A+", "4.00"
elif 85 <= marks < 90:
    grade, gpa = "A", "3.75"
elif 80 <= marks < 85:
    grade, gpa = "B+", "3.50"
elif 75 <= marks < 80:
    grade, gpa = "B", "3.25"
elif 70 <= marks < 75:
    grade, gpa = "C+", "3.00"
elif 65 <= marks < 70:
    grade, gpa = "C", "2.75"
elif 60 <= marks < 65:
    grade, gpa = "D+", "2.50"
elif 50 <= marks < 60:
    grade, gpa = "D", "2.25"
elif 0 <= marks < 50:
    grade, gpa = "F", "0.00"
else:
    grade, gpa = None, None

if grade:
    print(f"Marks: {marks:.2f} | Grade: {grade} | Grade Point: {gpa}")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")

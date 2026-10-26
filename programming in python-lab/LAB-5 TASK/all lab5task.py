# Exercise 1: Campus Resource Tracker
# Problem 1

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if len(resources) == 0:
        print("No resources found.")
        return

    for resource in resources:
        print(resource)


def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if not found:
        print("No resource found in this category.")


def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if not found:
        print("All resources are available.")



       



# Exercise 2: Student Marks Investigator
# Problem 2

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


def classify_performance(average):
    if average is None:
        return "Invalid marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]
        average = calculate_average(marks)
        performance = classify_performance(average)

        if average is None:
            print(student_id, name, "N/A", performance)
        else:
            print(student_id, name, round(average, 2), performance)





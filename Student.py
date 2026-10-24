def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to exit:").strip()
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
            marks = float(input("Enter marks for {name}:"))
            students[name] =marks
        except ValueError:
            print("please enter a valid number for marks")

    return students

def display_report(students):
    if not students:
        print("No student data")
        return
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks)/ len(marks)

    topper = [name for name,score in students.items()if score == max_score]
    bottomer = [name for name,score in students.items()if score == min_score]
    print("\n Student marks report ")
    print("-" * 30)
    print(f"total student : {len(students)}")
    print(f"average marks for  student : {average:.2f}")  #there will be two floting points it menas the after decimal there will be only two floating points
    print(f"Highest marks : {max_score} by {','.join(topper)}")
    print(f"lowest marks : {min_score} by {','.join(bottomer)}")

    print("-" * 30)
    print("Detailed marks ")
    for name,score in students.items():
        print(f"- {name} : {score}")

students = collect_student_data()
display_report(students)




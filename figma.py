SUBJECTS = ["Integral Calculus", "Physics", "Computer Programming", "Art Appreciation", "Science, Technology, and Society", "The Contemporary World", "Engineering Drawing", "PE"]

def add_student(students, name):
    if name not in students:
        students[name] = {}
        print(f"\nStudent {name} added successfully!")
    else:
        print(f"\nStudent {name} already exists.")

def add_subject_info(students, name, subject_index, grade, attendance):
    if name in students:
        if 0 <= subject_index < len(SUBJECTS):
            subject = SUBJECTS[subject_index]
            students[name][subject] = {'grade': grade, 'attendance': attendance}
            print(f"\nSubject {subject} info added to {name}.")
        else:
            print("\nInvalid subject index.")
    else:
        print(f"\nStudent {name} not found.")

def view_student(students, name):
    if name in students:
        print(f"\nPerformance for {name}:")
        if not students[name]:
            print("\nNo subjects recorded yet.")
        else:
            total_grade = 0
            subject_count = 0

            for subject, info in students[name].items():
                try:
                    grade = float(info['grade'])
                    total_grade += grade
                    subject_count += 1
                except ValueError:
                    print(f"\nInvalid grade for subject '{subject}'.")
                    continue

                print(f"   Subject: {subject}")
                print(f"     Grade: {info['grade']}%")
                print(f"Attendance: {info['attendance']}")
                print("-" * 35)

            if subject_count > 0:
                avg = total_grade / subject_count
                print(f"\nAverage Grade across all subjects: {avg:.2f}")
            else:
                print("\nNo valid grades to compute an average.")
    else:
        print(f"\nStudent {name} not found.")

def main():
    students = {}

    while True:
        print("\nWelcome to the Student Performance Tracker!")
        print("Please choose an option:")
        print("1. Add Student")
        print("2. Add Subject Grade and Attendance")
        print("3. View Student Performance")
        print("4. Exit")
        option = input("\nEnter your choice (1-4): ")

        if option == '1':
            name = input("\nEnter student name: ")
            add_student(students, name)
        elif option == '2':
            name = input("\nEnter student name: ")

            print("\nAvailable Subjects:")
            for i, subject in enumerate(SUBJECTS):
                print(f"{i + 1}. {subject}")
            try:
                subject_choice = int(input("\nEnter subject number: ")) - 1
                grade = input("\nEnter grade: ")
                attendance = input("\nEnter number of attendance: ")
                add_subject_info(students, name, subject_choice, grade, attendance)
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif option == '3':
            name = input("\nEnter student name: ")
            view_student(students, name)
        elif option == '4':
            print("\nThank you for using the Student Performance Tracker!")
            break
        else:
            print("\nInvalid choice. Please try again.")

main()
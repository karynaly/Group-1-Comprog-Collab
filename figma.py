SUBJECTS = ["Integral Calculus", "Physics", "Computer Programming", "Art Appreciation",
    "Science, Technology, and Society", "The Contemporary World",
    "Engineering Drawing", "PathFit"]

def add_student(students, name):
    if name not in students:
        students[name] = {}
        print(f"\nStudent {name} added successfully!")
    else:
        print(f"\nStudent {name} already exists.")

def generate_remarks(grade):
    if grade >= 95:
        return "Excellent"
    elif grade >= 90:
        return "Very Good"
    elif grade >= 85:
        return "Good"
    elif grade >= 80:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def add_subject_info(students, name, semester, subject_index, grade, attendance):
    if name in students:
        if 0 <= subject_index < len(SUBJECTS):
            subject = SUBJECTS[subject_index]
            if semester not in students[name]:
                students[name][semester] = {}

            grade = float(grade)
            remarks = generate_remarks(grade)

            students[name][semester][subject] = {
                'grade': grade,
                'attendance': attendance,
                'remarks': remarks
            }
            print(f"\nSubject {subject} info added to {name} in {semester}.")
        else:
            print("\nInvalid subject index.")
    else:
        print(f"\nStudent {name} not found.")

def update_subject_info(students, name, semester, subject_index, new_grade, new_attendance):
    if name in students and semester in students[name]:
        subject = SUBJECTS[subject_index]
        if subject in students[name][semester]:
            new_grade = float(new_grade)
            remarks = generate_remarks(new_grade)

            students[name][semester][subject] = {
                'grade': new_grade,
                'attendance': new_attendance,
                'remarks': remarks
            }
            print(f"\nSubject {subject} info updated for {name}.")
        else:
            print(f"\nSubject {subject} not found for {name} in {semester}.")
    else:
        print("\nStudent or semester not found.")

def view_student(students, name):
    if name in students:
        print(f"\nPerformance for {name}:")
        if not students[name]:
            print("\nNo semesters or subjects recorded yet.")
        else:
            total_grade = 0
            subject_count = 0

            for semester, subjects in students[name].items():
                print(f"\n  Semester: {semester}")
                for subject, info in subjects.items():
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
                    print(f"   Remarks: {info['remarks']}")
                    print("-" * 35)

            if subject_count > 0:
                avg = total_grade / subject_count
                print(f"\nAverage Grade across all subjects: {avg:.2f}")
            else:
                print("\nNo valid grades to compute an average.")
    else:
        print(f"\nStudent {name} not found.")

def search_student_by_name(students, keyword):
    matches = [name for name in students if keyword.lower() in name.lower()]
    if matches:
        print("\nMatching Students:")
        for name in matches:
            print(f" - {name}")
    else:
        print("\nNo matching students found.")

def view_top_performers(students):
    top_students = []

    for name, semesters in students.items():
        total = 0
        count = 0
        for subjects in semesters.values():
            for info in subjects.values():
                try:
                    total += float(info['grade'])
                    count += 1
                except ValueError:
                    continue
        if count > 0:
            avg = total / count
            if avg >= 90:
                top_students.append((name, avg))

    if top_students:
        print("\nTop Performers (With an Average of 90 and above):")
        for name, avg in sorted(top_students, key=lambda x: x[1], reverse=True):
            print(f" - {name}: {avg:.2f}")
    else:
        print("\nNo students have an average of 90 or above.")

def main():
    students = {}

    while True:
        print("\nWelcome to the Student Performance Tracker!")
        print("Please choose an option:")
        print("1. Add Student")
        print("2. Add Subject Grade and Attendance")
        print("3. View Student Performance")
        print("4. View Top Performer")
        print("5. Update Subject Info")
        print("6. Search Student by Name")
        print("7. Exit")
        option = input("\nEnter your choice (1-7): ").strip()

        if option == '1':
            name = input("\nEnter student name: ").strip()
            add_student(students, name)

        elif option == '2':
            name = input("\nEnter student name: ").strip()
            semester = input("\nEnter semester (Semester 1 or 2): ").strip()

            print("\nAvailable Subjects:")
            for i, subject in enumerate(SUBJECTS):
                print(f"{i + 1}. {subject}")

            try:
                subject_choice = int(input("\nEnter subject number: ")) - 1
                grade = float(input("\nEnter grade: "))
                attendance = input("\nEnter attendance count: ")
                add_subject_info(students, name, semester, subject_choice, grade, attendance)
            except ValueError:
                print("\nInvalid input. Please enter proper values.")

        elif option == '3':
            name = input("\nEnter student name: ").strip()
            view_student(students, name)

        elif option == '4':
            view_top_performers(students)
        
        elif option == '5':
            name = input("\nEnter student name: ").strip()
            semester = input("\nEnter semester: ").strip()

            print("\nAvailable Subjects:")
            for i, subject in enumerate(SUBJECTS):
                print(f"{i + 1}. {subject}")

            try:
                subject_choice = int(input("\nEnter subject number to update: ")) - 1
                grade = float(input("\nEnter new grade: "))
                attendance = input("\nEnter new attendance: ")
                update_subject_info(students, name, semester, subject_choice, grade, attendance)
            except ValueError:
                print("\nInvalid input.")

        elif option == '6':
            keyword = input("\nEnter name or part of name to search: ").strip()
            search_student_by_name(students, keyword)
            
        elif option == '7':
            print("\nThank you for using the Student Performance Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")

main()
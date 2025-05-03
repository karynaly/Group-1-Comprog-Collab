def add_student(students, name):
  if name not in students:
      students[name] = {}
      print(f"Student {name} added successfully!")
  else:
      print(f"Student {name} already exists.")

def add_subject_info(students, name, subject, grade, attendance):
  if name in students:
      students[name][subject] = {'grade': grade, 'attendance': attendance}
      print(f"Subject {subject} info added to {name}.")
  else:
      print(f"Student {name} not found.")

def view_student(students, name):
  if name in students:
      print(f"\nPerformance for {name}:")
      if not students[name]:
          print("No subjects recorded yet.")
      else:
          for subject, info in students[name].items():
              print(f"Subject: {subject}")
              print(f"  Grade: {info['grade']}")
              print(f"  Attendance: {info['attendance']}%")
              print("-" * 20)
  else:
      print(f"Student {name} not found.")

def main():
  students = {}

  while True:
      print("\nWelcome to the Student Performance Tracker!")
      print("\nPlease choose an option:")
      print("1. Add Student")
      print("2. Add Subject Info")
      print("3. View Student Performance")
      print("4. Exit")
      option = input("\nEnter your choice (1-4): ")

      if option == '1':
          name = input("\nEnter student name: ")
          add_student(students, name)
      elif option == '2':
          name = input("\nEnter student name: ")
          subject = input("\nEnter subject: ")
          grade = input("\nEnter grade: ")
          attendance = input("\nEnter number of attendance: ")
          add_subject_info(students, name, subject, grade, attendance)
      elif option == '3':
          name = input("\nEnter student name: ")
          view_student(students, name)
      elif option == '4':
          print("\nThank you for using the Student Performance Tracker!")
          break
      else:
          print("\nInvalid choice. Please try again.")

main()
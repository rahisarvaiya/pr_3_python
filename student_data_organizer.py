students_list = []
student_dict = {}
all_subjects = set()

def display_menu():
    print("\n" + "=" * 50)
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print("=" * 50)

def add_student():
    print("\n--- Add Student ---")
    try:
        student_id = int(input("Student ID: "))
        if student_id in student_dict:
            print(f"Error: Student ID {student_id} already exists.")
            return
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return

    name = input("Name: ").strip()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age. Please enter an integer.")
        return
    grade = input("Grade: ").strip()
    dob = input("Date of Birth (YYYY-MM-DD): ").strip()
    subjects_input = input("Subjects (comma-separated): ").strip()

    subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]
    all_subjects.update(subjects)

    id_dob_tuple = (student_id, dob)

    student_record = {
        'id_dob': id_dob_tuple,
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects
    }

    students_list.append(student_record)
    student_dict[student_id] = student_record

    print(f"\nStudent added successfully! (ID: {student_id})")

def display_all_students():
    print("\n--- All Students ---")
    if not students_list:
        print("No student records found.")
        return

    for record in students_list:
        sid, dob = record['id_dob']
        print(f"Student ID: {sid} | Name: {record['name']} | Age: {record['age']} | "
              f"Grade: {record['grade']} | Subjects: {', '.join(record['subjects'])}")

def update_student():
    print("\n--- Update Student Information ---")
    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    if student_id not in student_dict:
        print(f"Student ID {student_id} not found.")
        return

    record = student_dict[student_id]
    print(f"Current details: Name: {record['name']}, Age: {record['age']}, "
          f"Grade: {record['grade']}, Subjects: {', '.join(record['subjects'])}")

    print("What would you like to update?")
    print("1. Age")
    print("2. Subjects")
    choice = input("Enter choice (1/2): ").strip()

    if choice == '1':
        try:
            new_age = int(input("Enter new age: "))
            record['age'] = new_age
            print("Age updated successfully.")
        except ValueError:
            print("Invalid age.")
    elif choice == '2':
        subjects_input = input("Enter new subjects (comma-separated): ").strip()
        new_subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]
        record['subjects'] = new_subjects
        all_subjects.update(new_subjects)
        print("Subjects updated successfully.")
    else:
        print("Invalid choice.")

def delete_student():
    print("\n--- Delete Student ---")
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    if student_id not in student_dict:
        print(f"Student ID {student_id} not found.")
        return

    del student_dict[student_id]

    global students_list
    students_list = [rec for rec in students_list if rec['id_dob'][0] != student_id]

    print(f"Student ID {student_id} deleted successfully.")

def display_subjects():
    print("\n--- Unique Subjects Offered ---")
    if not all_subjects:
        print("No subjects recorded yet.")
    else:
        for subj in sorted(all_subjects):
            print(f"- {subj}")

def main():
    print("=" * 60)
    print("Welcome to the Student Data Organizer!")
    print("=" * 60)
    print("This program manages student records using lists, tuples,")
    print("sets, and dictionaries. You can add, display, update, delete")
    print("students and view all unique subjects offered.\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects()
        elif choice == '6':
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
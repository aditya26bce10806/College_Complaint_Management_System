from validation import validate_complaint
from database import add_complaint, get_student_complaints


def student_dashboard(username):
    while True:
        print("\n===== STUDENT DASHBOARD =====")
        print("1. Submit Complaint")
        print("2. View My Complaints")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            submit_complaint(username)

        elif choice == "2":
            view_complaints(username)

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def submit_complaint(username):
    print("\n===== SUBMIT COMPLAINT =====")

    print("\nSelect Complaint Category:")
    print("1. Hostel")
    print("2. Mess")
    print("3. Academic")
    print("4. Infrastructure")
    print("5. Other")

    category_choice = input("Enter category choice: ")

    categories = {
        "1": "Hostel",
        "2": "Mess",
        "3": "Academic",
        "4": "Infrastructure",
        "5": "Other"
    }

    if category_choice not in categories:
        print("Invalid category choice.")
        return

    category = categories[category_choice]

    print("\nSelect Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Enter priority choice: ")

    priorities = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    if priority_choice not in priorities:
        print("Invalid priority choice.")
        return

    priority = priorities[priority_choice]

    subject = input("\nEnter complaint subject: ")
    description = input("Enter complaint description: ")

    is_valid, message = validate_complaint(subject, description)

    if not is_valid:
        print(message)
        return

    complaint_id = add_complaint(
        username,
        category,
        priority,
        subject,
        description
    )

    print("\nComplaint submitted successfully!")
    print("Complaint ID:", complaint_id)
    print("Complaint Status: Pending")


def view_complaints(username):
    print("\n===== MY COMPLAINTS =====")

    student_complaints = get_student_complaints(username)

    if len(student_complaints) == 0:
        print("No complaints found.")
        return

    for complaint in student_complaints:
        print(f"\nComplaint ID: {complaint[0]}")
        print("Student:", complaint[1])
        print("Category:", complaint[2])
        print("Priority:", complaint[3])
        print("Subject:", complaint[4])
        print("Description:", complaint[5])
        print("Status:", complaint[6])
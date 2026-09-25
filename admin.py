from database import (get_all_complaints,update_complaint_status as update_status_in_database)
from reports import complaint_report


def admin_dashboard():
    while True:
        print("\n===== ADMIN DASHBOARD =====")
        print("1. View All Complaints")
        print("2. Update Complaint Status")
        print("3. Complaint Report")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_complaints()

        elif choice == "2":
            update_complaint_status()

        elif choice == "3":
            complaint_report()

        elif choice == "4":
            print("Admin logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def view_all_complaints():
    print("\n===== ALL COMPLAINTS =====")

    complaints = get_all_complaints()

    if len(complaints) == 0:
        print("No complaints found.")
        return

    for complaint in complaints:
        print(f"\nComplaint ID: {complaint[0]}")
        print("Student:", complaint[1])
        print("Category:", complaint[2])
        print("Priority:", complaint[3])
        print("Subject:", complaint[4])
        print("Description:", complaint[5])
        print("Status:", complaint[6])


def update_complaint_status():
    print("\n===== UPDATE COMPLAINT STATUS =====")

    complaints = get_all_complaints()

    if len(complaints) == 0:
        print("No complaints found.")
        return

    view_all_complaints()

    try:
        complaint_id = int(input("\nEnter Complaint ID: "))

        complaint_exists = False

        for complaint in complaints:
            if complaint[0] == complaint_id:
                complaint_exists = True
                break

        if not complaint_exists:
            print("Invalid Complaint ID.")
            return

        print("\nSelect new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Resolved")

        status_choice = input("Enter your choice: ")

        if status_choice == "1":
            status = "Pending"

        elif status_choice == "2":
            status = "In Progress"

        elif status_choice == "3":
            status = "Resolved"

        else:
            print("Invalid status choice.")
            return

        update_status_in_database(complaint_id, status)

        print("Complaint status updated successfully!")

    except ValueError:
        print("Please enter a valid Complaint ID.")
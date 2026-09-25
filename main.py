from login import student_login, admin_login
from student import student_dashboard
from admin import admin_dashboard
from database import create_database

create_database()

def main():

    while True:

        print("\n===== COLLEGE COMPLAINT MANAGEMENT SYSTEM =====")
        print("1. Student Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = student_login()

            if username:
                student_dashboard(username)

        elif choice == "2":
            if admin_login():
                admin_dashboard()

        elif choice == "3":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
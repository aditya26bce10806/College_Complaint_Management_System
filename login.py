def student_login():
    username = input("Enter Student Username: ")
    password = input("Enter Password: ")

    if username == "student" and password == "1234":
        print("Student Login Successful")
        return username
    else:
        print("Invalid Username or Password")
        return None


def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "admin123":
        print("Admin Login Successful")
        return True
    else:
        print("Invalid Username or Password")
        return False
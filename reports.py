from database import get_all_complaints


def complaint_report():
    print("\n===== COMPLAINT REPORT =====")

    complaints = get_all_complaints()

    total = len(complaints)

    pending = 0
    in_progress = 0
    resolved = 0

    low = 0
    medium = 0
    high = 0

    for complaint in complaints:

        if complaint[6] == "Pending":
            pending += 1

        elif complaint[6] == "In Progress":
            in_progress += 1

        elif complaint[6] == "Resolved":
            resolved += 1

        if complaint[3] == "Low":
            low += 1

        elif complaint[3] == "Medium":
            medium += 1

        elif complaint[3] == "High":
            high += 1

    print("Total Complaints:", total)

    print("\n----- Complaint Status -----")
    print("Pending:", pending)
    print("In Progress:", in_progress)
    print("Resolved:", resolved)

    print("\n----- Complaint Priority -----")
    print("Low:", low)
    print("Medium:", medium)
    print("High:", high)
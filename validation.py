def validate_complaint(subject, description):
    if subject.strip() == "":
        return False, "Complaint subject cannot be empty."

    if description.strip() == "":
        return False, "Complaint description cannot be empty."

    if len(subject.strip()) < 3:
        return False, "Complaint subject must contain at least 3 characters."

    if len(description.strip()) < 10:
        return False, "Complaint description must contain at least 10 characters."

    return True, "Valid complaint."
from task_7 import Instructor


def main():
    instructor = Instructor("Doe", "John", {})
    print(instructor)  # Doe John

    instructor.add_semester(1, ["Math", "Physics"])
    instructor.add_semester(2, ["Chemistry"])
    instructor.add_subject_to_semester("Biology", 1)
    instructor.add_subjects(2)
    instructor.remove_subject_from_semester("Math", 1)
    instructor.print_semester_subjects(1)  # Number of subjects in semester 1: 2
    # Subjects in semester 1:
    # Physics
    # Biology

    instructor.print_average_subjects()  # Average number of subjects per semester: 1.3333333333333333
    instructor.print_semester_with_most_subjects()  # Semester with the most subjects: 1
    # Number of subjects in semester 1: 2

    instructor.print_subjects_per_semester()  # Subjects per semester:
    # Semester 1: 2 subjects
    #     Physics
    #     Biology
    # Semester 2: 1 subjects
    #     Chemistry

    instructor.add_semester_with_subjects()  # Enter a semester number: 3
    # Enter a subject for this semester (or 'done' to finish): History
    # Enter a subject for this semester (or 'done' to finish): Geography
    # Enter a subject for this semester (or 'done' to finish): done
    # Added 2 subjects to semester 3

    instructor.remove_semester(2)
    instructor.print_subjects_per_semester()  # Subjects per semester:
    # Semester 1: 2 subjects
    #     Physics
    #     Biology
    # Semester 3: 2 subjects
    #     History
    #     Geography


if __name__ == "__main__":
    main()

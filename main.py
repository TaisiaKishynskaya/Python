from task_7 import Instructor


def main():
    instructors = [
        Instructor('Doe', 'John', {}),
        Instructor('Smith', 'Jane', {}),
        Instructor('Brown', 'Michael', {}),
    ]

    for instructor in instructors:
        print(instructor)  # Prints name and surname of the instructor

        # Add semesters and subjects to the instructor's schedule
        instructor.update_semester(1, ['Math', 'Physics'])
        instructor.update_semester(2, ['Chemistry'])
        instructor.add_subject_to_semester('Biology', 1)
        instructor.add_subjects(2)
        instructor.remove_subject_from_semester('Math', 1)
        instructor.print_semester_subjects(1)  # Number of subjects in semester 1: 2

        # Print statistics about the instructor's schedule
        instructor.print_average_subjects()  # Average number of subjects per semester
        instructor.print_semester_with_most_subjects()  # Semester with the most subjects
        instructor.print_subjects_per_semester()  # List of subjects per semester

        # Add a semester with user input
        instructor.add_semester_with_subjects()

        # Remove a semester
        instructor.update_semester(2)

        # Remove subjects from a semester with user input
        semester_num = int(input('Enter the semester number to remove subjects from: '))
        subjects_to_remove = []
        while True:
            subject = input("Enter a subject to remove from the semester (or 'done' to finish): ")
            if subject == 'done':
                break
            subjects_to_remove.append(subject)
        instructor.remove_subject_from_semester(subjects_to_remove, semester_num)
        instructor.print_semester_subjects(semester_num)


if __name__ == "__main__":
    main()

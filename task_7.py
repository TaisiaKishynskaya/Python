class Instructor:
    def __init__(self, last_name, first_name, subjects_per_semester):
        self.last_name = last_name
        self.first_name = first_name
        self.subjects_per_semester = subjects_per_semester

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def add_subject_to_semester(self, subject, semester):
        subjects = self.subjects_per_semester.get(semester, [])
        subjects.append(subject)
        self.subjects_per_semester[semester] = subjects

    def remove_subject_from_semester(self, subject, semester):
        subjects = self.subjects_per_semester.get(semester, [])
        if subject in subjects:
            subjects.remove(subject)
            self.subjects_per_semester[semester] = subjects

    def add_semester(self, semester, subjects=[]):
        self.subjects_per_semester[semester] = subjects

    def remove_semester(self, semester):
        del self.subjects_per_semester[semester]

    def print_semester_subjects(self, semester):
        subjects = self.subjects_per_semester.get(semester, [])
        print(f"Number of subjects in semester {semester}: {len(subjects)}")
        print(f"Subjects in semester {semester}:")
        for subject in subjects:
            print(subject)

    def print_average_subjects(self):
        num_semesters = len(self.subjects_per_semester)
        num_subjects = sum(len(subjects) for subjects in self.subjects_per_semester.values())
        print(f"Average number of subjects per semester: {num_subjects / num_semesters}")

    def print_semester_with_most_subjects(self):
        max_subjects = -1
        max_semester = None
        for semester, subjects in self.subjects_per_semester.items():
            num_subjects = len(subjects)
            if num_subjects > max_subjects:
                max_subjects = num_subjects
                max_semester = semester
        print(f"Semester with the most subjects: {max_semester}")
        print(f"Number of subjects in semester {max_semester}: {max_subjects}")

    def print_subjects_per_semester(self):
        print("Subjects per semester:")
        for semester, subjects in self.subjects_per_semester.items():
            print(f"Semester {semester}: {len(subjects)} subjects")
            for subject in subjects:
                print(f"\t{subject}")

    def add_subjects(self, semester):
        subjects = self.subjects_per_semester.get(semester, [])
        while True:
            subject = input("Enter a subject to add or 'done' to finish: ")
            if subject.lower() == 'done':
                break
            subjects.append(subject)
        self.subjects_per_semester[semester] = subjects

    def remove_subjects(self, semester):
        subjects = self.subjects_per_semester.get(semester, [])
        while True:
            subject = input("Enter a subject to remove or 'done' to finish: ")
            if subject.lower() == 'done':
                break
            if subject in subjects:
                subjects.remove(subject)
        self.subjects_per_semester[semester] = subjects

    def add_semester_with_subjects(self):
        semester = input("Enter a semester number: ")
        subjects = []
        while True:
            subject = input("Enter a subject for this semester (or 'done' to finish): ")
            if subject == 'done':
                break
            subjects.append(subject)
        self.subjects_per_semester[semester] = subjects
        print(f"Added {len(subjects)} subjects to semester {semester}")

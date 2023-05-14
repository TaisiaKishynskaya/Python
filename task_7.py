def validate_semester_number(semester):
    if not isinstance(semester, int) or semester <= 0:
        raise ValueError("Semester number must be a positive integer")


def validate_semester_exists(semester, subjects_per_semester):
    if semester not in subjects_per_semester:
        raise ValueError(f"Semester {semester} does not exist")


class Instructor:
    def __init__(self, last_name, first_name, subjects_per_semester):
        self._last_name = last_name
        self._first_name = first_name
        self._subjects_per_semester = subjects_per_semester

    def __str__(self):
        return f'{self._last_name} {self._first_name}'

    def add_subject_to_semester(self, subject, semester, subjects_per_semester=None):
        validate_semester_number(semester)
        validate_semester_exists(semester, subjects_per_semester)
        self._subjects_per_semester.setdefault(semester, []).append(subject)

    def remove_subject_from_semester(self, subject, semester, subjects_per_semester=None):
        validate_semester_number(semester)
        validate_semester_exists(semester, subjects_per_semester)
        subjects = self._subjects_per_semester.get(semester, [])
        if subject in subjects:
            subjects.remove(subject)
        else:
            raise ValueError(f'{subject} not found in semester {semester}')
        self._subjects_per_semester[semester] = subjects

    def update_semester(self, semester, subjects=None, subjects_per_semester=None):
        validate_semester_number(semester)  # validation
        if semester in self._subjects_per_semester and subjects is not None:
            raise ValueError(f'Semester {semester} already exists')
        validate_semester_exists(semester, subjects_per_semester)
        self._subjects_per_semester[semester] = subjects

    def print_semester_subjects(self, semester):
        subjects = self._subjects_per_semester.get(semester, [])
        print(f'Number of subjects in semester {semester}: {len(subjects)}')
        print(f'Subjects in semester {semester}:')
        for subject in subjects:
            print(subject)

    def print_average_subjects(self):
        num_semesters = len(self._subjects_per_semester)
        num_subjects = sum(len(subjects) for subjects in self._subjects_per_semester.values())
        print(f'Average number of subjects per semester: {num_subjects / num_semesters}')

    @property
    def semester_with_most_subjects(self):
        return  max(self._subjects_per_semester.keys(),
                           key=lambda semester: len(self._subjects_per_semester[semester]))

    def print_semester_with_most_subjects(self):
        max_semester = self.semester_with_most_subjects
        print(f'Semester with the most subjects: {max_semester}')
        print(f'Number of subjects in semester {max_semester}: {len(self._subjects_per_semester[max_semester])}')

    def print_subjects_per_semester(self):
        print('Subjects per semester:')
        for semester, subjects in self._subjects_per_semester.items():
            print(f'Semester {semester}: {len(subjects)} subjects')
            for subject in subjects:
                print(f'\t{subject}')

    def _get_subjects(self, semester, subjects_per_semester=None):
        validate_semester_exists(semester, subjects_per_semester)
        return self._subjects_per_semester.setdefault(semester, [])

    def add_subjects(self, semester, subjects_per_semester=None):
        subjects = self._get_subjects(semester, subjects_per_semester)
        while True:
            subject = input("Enter a subject to add or 'done' to finish: ")
            if subject.lower() == 'done':
                break
            subjects.append(subject)
        self._subjects_per_semester[semester] = subjects

    def remove_subjects(self, semester, subjects_per_semester=None):
        subjects = self._get_subjects(semester, subjects_per_semester)
        while True:
            subject = input("Enter a subject to remove or 'done' to finish:")
            if subject.lower() == 'done':
                break
            if subject in subjects:
                subjects.remove(subject)
            else:
                print(f'{subject} is not found in semester {semester}')
        self._subjects_per_semester[semester] = subjects
        print(f'Removed {len(subjects)} subjects from semester {semester}')

    def add_semester_with_subjects(self):
        semester = input('Enter a semester number: ')
        try:
            semester = int(semester)
        except ValueError:
            print('Invalid semester number. Please enter an integer.')
            return
        if semester not in self._subjects_per_semester:
            self._subjects_per_semester[semester] = []
        else:
            print(f'Semester {semester} already exists. Adding subjects to existing semester.')
        while True:
            subject = input("Enter a subject for this semester (or 'done' to finish): ")
            if subject == 'done':
                break
            self._subjects_per_semester[semester].append(subject)
        print(f'Added {len(self._subjects_per_semester[semester])} subjects to semester {semester}')

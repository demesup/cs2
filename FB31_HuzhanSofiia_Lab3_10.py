class Instructor:
    def __init__(self, last_name, first_name, subjects):
        self.last_name = last_name
        self.first_name = first_name
        self.subjects = subjects

    def __str__(self):
        return self.last_name + " " + self.first_name + ", subjects:" + str(self.subjects)

    def count_subjects(self, semester):
        return len(self.subjects[semester])

    def moda_subjects(self):
        semester_count = len(self.subjects)
        subject_count = 0
        for key, value in self.subjects.items():
            subject_count += len(value)

        return subject_count / semester_count

    def max_subjects(self):
        max_semester = -1
        max_semester_length = -1
        for key, value in self.subjects.items():
            if len(value) > max_semester_length:
                max_semester_length = len(value)
                max_semester = key
        return max_semester, max_semester_length

    def add_subject(self, semester, subject):
        if semester not in self.subjects:
            self.subjects[semester] = []
        if subject not in self.subjects[semester]:
            self.subjects[semester].append(subject)

    def remove_subject(self, semester, subject):
        if semester in self.subjects:
            if subject in self.subjects[semester]:
                self.subjects[semester].remove(subject)


instructor = Instructor("Shevchenko", "Daria",
                        {"Autumn 2023": ["Python", "Math"], "Spring 2024": ["Java", "Physics", "Math 2"]})


instructor2 = Instructor("Kuzmenko", "Vlasislav", {})
print(instructor)
print(instructor2)

print(f"Number of courses in Autumn 2023: {instructor.count_subjects('Autumn 2023')}")

print(f"Average number of courses: {instructor.moda_subjects()}")
print(f"Max number of courses: {instructor.max_subjects()}")

instructor.add_subject("Autumn 2022", "C++")
print(f"\nAfter adding C++ to Autumn 2022\n{instructor}\n")
instructor.add_subject("Autumn 2022", "C++")
print(f"After adding C++ to Autumn 2022\n{instructor}\n")

instructor.remove_subject("Autumn 2022", "Lalala")
print(f"After removing Lalala from Autumn 2022\n{instructor}\n")
instructor.remove_subject("Autumn 2022", "C++")
print(f"After removing C++ from Autumn 2022\n{instructor}\n")

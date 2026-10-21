# TASK 5 - PYTHON MODULE

class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        result = "Pass" if self.passed() else "Fail"
        return f"{self.name} ({self.marks}): {result}"


class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, name, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError(
                f"Invalid marks for {name}: {marks}"
            )

        student = Student(name, marks)
        self.students.append(student)

    def average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.marks

        return total / len(self.students)

    def top_student(self):
        if len(self.students) == 0:
            return None

        top = max(
            self.students,
            key=lambda student: student.marks
        )
        return top.name

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return (
            f"{self.title}: {len(self)} students, "
            f"average {self.average():.1f}"
        )


def load_course(filename):
    course = Course("Programming for AI")

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    name, marks = line.split(",")
                    name = name.strip()
                    marks = int(marks.strip())
                    course.add_student(name, marks)

                except ValueError:
                    print("Skipping invalid data:", line)

                except InvalidMarksError as e:
                    print("Skipping:", e)

    except FileNotFoundError:
        print("File not found:", filename)

    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("Ali", 50)
    print(test)
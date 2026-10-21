# PROGRAMMING FOR AI - LAB 1
# MAIN FILE

from course import Student, Course, InvalidMarksError, load_course


# TASK 1 - STUDENT CLASS
print("\n--- TASK 1 ---")

student1 = Student("Ali", 72)
student2 = Student("Sara", 45)
student3 = Student("Omar", 50)

print(student1)
print(student2)
print(student3)


# TASK 2 - COURSE CLASS
print("\n--- TASK 2 ---")

course = Course("Programming for AI")

course.add_student("Ali", 88)
course.add_student("Sara", 92)
course.add_student("Omar", 75)

print("Course:", course.title)
print("Total Students:", len(course))
print("Average Marks:", course.average())
print("Top Student:", course.top_student())


# TASK 3 - CUSTOM EXCEPTION
print("\n--- TASK 3 ---")

try:
    course.add_student("Bilal", 120)

except InvalidMarksError as e:
    print("Error:", e)

print("Total Students:", len(course))


# TASK 4 - FILE HANDLING
print("\n--- TASK 4 ---")

loaded_course = load_course("marks.txt")

print(loaded_course)
print("Top Student:", loaded_course.top_student())

load_course("mark.txt")


# TASK 5 - MODULES
print("\n--- TASK 5 ---")
print("Modules imported successfully!")
print("All tasks completed!")
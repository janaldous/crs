"""
Student, Admin, Teacher objects go here
"""

courses = []
students = []
admins = []
teachers = []

class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "User: %s" % (self.name)


class Student(User):
    # static variable to keep track of number of students
    student_ctr = 0

    def __init__(self, name, year_level):
        self.name = name
        self.year_level = year_level
        self.student_number = Student.student_ctr
        Student.student_ctr += 1
        self.courses = []

    def enroll_to_class(self, course):
        course.add_student(self)

    def view_grades(self, course):
        for c in self.courses:
            print("course:%s, grade:%s" % (c.name, c.get_grade(self)))

    def calculate_gwa(self):
        total = 0
        num_of_classes = len(self.courses)
        for course in self.courses:
            total += course.get_grade(self)

        if num_of_classes == 0:
            return "n/a"

        return total / num_of_classes

    def __str__(self):
        return "Student: {name:%s, year_level:%s, student_number:%s, gwa:%s}" % (self.name,
                                                                                 self.year_level, self.student_number,
                                                                                 self.calculate_gwa())


class Teacher(User):
    # static variable to keep track of number of employees
    employee_ctr = 0

    def __init__(self, name):
        self.name = name
        self.employee_number = Teacher.employee_ctr
        Teacher.employee_ctr += 1
        self.courses = []

    def print_courses(self):
        for course in self.courses:
            print(course)

    def submit_grades(self):
        #choose course first
        course_index = int(self.get_course_from_list())
        #choose student
        course = self.courses[course_index]
        student_index = int(course.get_student_from_list())
        #set grade
        grade = int(input("Enter grade: "))
        course.set_grade_via_index(student_index, grade)
        print(course.students[0])

    def get_course_from_list(self):
        for index, course in enumerate(self.courses):
            print("[%s] %s" % (index, course))
            #TODO validate input
        return input("Enter id of course: ")

    def __str__(self):
        return "Student: {name:%s, year_level:%s, student_number:%s, gwa:%s}" % (self.name,
                                                                                 self.year_level, self.student_number,
                                                                                 self.gwa)

class Admin(User):
    def create_course(self, name, quota):
        course = Course(name, quota)
        courses.append(course)
        return course

    def create_teacher(self, name):
        teacher = Teacher(name)
        teachers.append(teacher)
        return teacher

    def create_student(self, name, year_level):
        student = Student(name, year_level)
        students.append(student)
        return student

    def create_schedule(self):
        #student, teacher cannot be in the same block
        # only 3 classes per day per student
        # Schedule: 8 blocks
        day = Day()
        day.add

class Course(object):
    def __init__(self, name, quota):
        self.name = name
        self.quota = quota
        self.students = []

    def __str__(self):
        return "Course: {name:%s, quota:%s}" % (self.name, self.quota)

    def is_full(self):
        if len(self.students) < self.quota:
            return False
        else:
            return True

    def add_student(self, new_student):
        """
        appends new student to student list
        :param new_student: Student object
        :return:
        """

        #TODO raise Error
        if (self.is_full()):
            print("is full")
        else:
            grade_dict = {
                'student':new_student,
                'grade': False,
            }
            self.students.append(grade_dict)
            new_student.courses.append(self)
            print("added student")

    def remove_student(self, student):
        for st in self.students:
            if st['student'] == student:
                self.students.remove(st)
        # TODO if student exists, error

    def set_teacher(self, teacher):
        self.teacher = teacher
        teacher.courses.append(self)
        # TODO if teacher already exists,warn user

    def set_grade(self, student, grade):
        if grade > 100:
            #TODO correct error
            raise ArithmeticError
        elif grade < 0:
            #TODO correct error
            raise ArithmeticError
        for st in self.students:
            if st['student'] == student:
                st['grade'] = grade

    def set_grade_via_index(self, index, grade):
        student = self.students[index]['student']
        self.set_grade(student, grade)

    def get_grade(self, student):
        for st in self.students:
            if st['student'] == student:
                return st['grade']

    def get_student_from_list(self):
        if len(self.students) == 0:
            return "There are no students in this course"
        for index, student in enumerate(self.students):
            print("[%s] %s" % (index, str(student['student'])))

        inp = int(input("Enter id of student: "))
        if not inp in range(len(student)-1):
            raise IndexError
        return inp

    def has_student(self, student):
        for st in self.students:
            if st['student'] == student:
                return True
        return False

class Block(object):
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def can_add_course(self, course):
        #check if has same students as courses
        for c in courses:
            print(c.students)
            for student in course.students:
                print(student)
                if c.has_student(student):
                    return False
        return True

class Day(object):
    def __init__(self):
        self.block_1 = Block()
        self.block_2 = Block()
        self.block_3 = Block()
        self.block_4 = Block()
        self.block_5 = Block()
        self.block_6 = Block()
        self.blocks = [self.block_1, self.block_2, self.block_3, self.block_4, self.block_5, self.block_6]

    def add_course(self, course):
        for block in self.blocks:
            pass

class Schedule(object):
    def __init__(self):
        self.mon = Day()
        self.tue = Day()
        self.wed = Day()
        self.thu = Day()
        self.fri = Day()
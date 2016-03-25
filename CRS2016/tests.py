import unittest

from objects import Student, Course, Teacher, Admin, courses, teachers, students, Block


class TestCase2(unittest.TestCase):

  def test_add_student(self):
      s = Student("jat", 1)
      c = Course("SEG", 1)
      c.add_student(s)

      self.assertEqual(len(c.students), 1, "Doesnt add student")



class TestCase1(unittest.TestCase):
    def test_add_student(self):
        s = Student("jat", 1)
        c = Course("SEG", 1)
        c.add_student(s)

        self.assertEqual(len(c.students), 1, "test pass")

    def test_add_student2(self):
        c = Course("SEG", 2)
        s = Student("jat", 1)
        s.enroll_to_class(c)

        self.assertEqual(len(c.students), 1)

    def test_add_teacher(self):
        c = Course("SEG", 2)
        t = Teacher("jat")
        c.set_teacher(t)

        self.assertEqual(c.teacher, t)

    def test_teacher_view_assigned_courses(self):
        c = Course("SEG", 2)
        c2 = Course("PLD", 2)
        t = Teacher("jat")
        c.set_teacher(t)
        c2.set_teacher(t)

        t.print_courses()

    def test_remove_student_from_course(self):
        c = Course("SEG", 2)
        s = Student("jat", 1)
        c.add_student(s)
        c.remove_student(s)

        print(len(c.students))
        self.assertEqual(len(c.students), 0)

    def save_grade(self):
        c = Course("SEG", 2)
        s = Student("jat", 1)
        c.add_student(s)
        c.set_grade(s, 1)

        self.assertEqual(c.students[0]['grade'], 1)

    def student_test_save_grade_upper_bound(self):
        pass

    def student_test_save_grade_lower_bound(self):
        pass

    def student_view_grade(self):
        c2 = Course("PLD", 2)
        c = Course("SEG", 2)
        s = Student("jat", 1)
        c.add_student(s)
        c2.add_student(s)
        c.set_grade(s, 100)
        c2.set_grade(s, 100)

        s.view_grades(c)
        #check console

    def test_submit_grades(self):
        c1 = Course("PLD", 2)
        c2 = Course("SEG", 2)

        t = Teacher("jat")
        s = Student("jat", 1)
        s2 = Student("s2", 1)

        c1.set_teacher(t)
        c2.set_teacher(t)
        c1.add_student(s)
        c2.add_student(s)
        c2.add_student(s2)

        c1.set_grade_via_index(0, 90)
        self.assertEqual(c1.students[0]['grade'], 90)
        #t.submit_grades()

    def test_calc_gwa_without_classes(self):
        s2 = Student("s2", 1)
        self.assertEqual(s2.calculate_gwa(), "n/a")


    def test_calc_gwa_with_classes(self):
        c1 = Course("PLD", 2)
        c2 = Course("SEG", 2)

        t = Teacher("jat")
        s = Student("jat", 1)
        s2 = Student("s2", 1)

        c1.set_teacher(t)
        c2.set_teacher(t)
        c1.add_student(s)
        c2.add_student(s)
        c2.add_student(s2)

        c1.set_grade_via_index(0, 100)
        c2.set_grade_via_index(0, 90)
        self.assertEqual(s.calculate_gwa(), 95)

    def test_admin_add_course(self):
        a = Admin("n")
        a.create_course("c", 1)

        self.assertEqual(len(courses), 1)

    def test_admin_add_teacher(self):
        a = Admin("n")
        a.create_teacher("c")

        self.assertEqual(len(teachers), 1)

    def test_admin_add_student(self):
        a = Admin("n")
        a.create_student("c", 5)

        self.assertEqual(len(students), 1)

    def test_course_has_student(self):
        c1 = Course("PLD", 2)

        s = Student("jat", 1)

        c1.add_student(s)

        self.assertEqual(c1.has_student(s), True)

    def test_block_can_add_course(self):
        c1 = Course("PLD", 2)
        s = Student("jat", 1)
        c1.add_student(s)

        b = Block()

        self.assertEqual(b.can_add_course(c1), True)

    def test_block_cannot_add_course2(self):
        c1 = Course("PLD", 2)
        c2 = Course("PLD", 2)
        s = Student("jat", 1)
        c1.add_student(s)
        c2.add_student(s)

        b = Block()
        b.add_course(c1)
        self.assertEqual(b.can_add_course(c2), False)

    def test_index_error(self):
        c1 = Course("PLD", 2)
        s = Student("jat", 1)
        c1.add_student(s)

        with self.assertRaises(IndexError):
            #TODO mock input of "1"
            c1.get_student_from_list()

if __name__ == '__main__':
    unittest.main()
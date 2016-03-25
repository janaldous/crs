import unittest

from objects import Student, Course


class TestCase1(unittest.TestCase):

  def test_add_student(self):
      s = Student("jat", 1)
      c = Course("SEG", 1)
      c.add_student(s)

      self.assertEqual(len(c.students), 1, "Doesnt add student")


if __name__ == '__main__':
    unittest.main()
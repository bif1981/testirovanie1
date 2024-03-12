import unittest
from main import Student


class TestStudent(unittest.TestCase):

    def test_walk_method(self):
        student = Student("Ildus")
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, "Distances are not equal (Расстояния не равны!)")

    def test_run_method(self):
        student = Student("Alex")
        for _ in range(5):
            student.run()
        self.assertEqual(student.distance, 50, "Distances are not equal (Расстояния не равны!)")

    def test_walk_and_run_methods(self):
        student = Student("Elena")
        student.walk()
        student.run()
        self.assertEqual(student.distance, 15, "Distances are not equal (Расстояния не равны!)")


if __name__ == '__main__':
    unittest.main()
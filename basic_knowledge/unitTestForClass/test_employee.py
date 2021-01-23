import unittest
from employeeClass import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        firstName = 'Dan'
        lastName = 'Jay'
        salary = 5000
        self.new_employee = Employee(firstName, lastName, salary)

    def test_default_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 10000)

    def test_custom_raise(self):
        self.new_employee.give_raise(1000)
        self.assertEqual(self.new_employee.salary, 6000)


unittest.main()

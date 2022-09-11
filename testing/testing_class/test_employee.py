import unittest
from employee import Employee


class TestEmployeeRaise(unittest.TestCase):
    """Test for default raise and custom raise"""

    def setUp(self) -> None:
        self.my_survey = Employee('Ziya', 'Alim', 10000)

    def test_give_default_raise(self):
        salary_raise = 5000
        base_salary = 10000
        self.my_survey.give_raise()
        self.assertEqual(self.my_survey.annual_salary, base_salary + salary_raise)

    def test_give_custom_raise(self):
        salary_raise = 9000
        base_salary = 10000
        self.my_survey.give_raise(salary_raise)
        self.assertEqual(self.my_survey.annual_salary, base_salary + salary_raise)


if __name__ == '__main__':
    unittest.main()

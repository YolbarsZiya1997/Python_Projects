class Employee:
    """A simple attempt to imitate an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=''):
        """If the raise are other than 5000 input salary raise, if not just add 5000"""
        if salary_raise:
            self.annual_salary = self.annual_salary + int(salary_raise)
        else:
            self.annual_salary += 5000

class Employee:
    '''general employee class with first name, last name, and yearly salary'''

    def __init__(self, firstName: str, lastName: 'str', salary) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def give_raise(self, salary_raise: int = 5000):
        self.salary += salary_raise

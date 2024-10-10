from skpractice.employeeinheritance.employee import Employee


class SalaryEmployee(Employee):

    def __init__(self, name: str, age: int, role: str, salary: float):
        super().__init__(name, age, role)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"""
        {super().__str__()}Salary: {self.salary}
        """

jonah = SalaryEmployee("Jonah", 43, "engineer", 2500000.00)
print(jonah.__str__())
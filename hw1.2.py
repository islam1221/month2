
class Employee:
    emp_count = 0
    work_rate = 2

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        pass

    def display_eployee(self):
        print(f"Мое новое имя:{self.name} \nЗарплата:{self.salary} ")

    def change_name(self, new_name):
        self.name = new_name

    def get_total_salary(self):
        return self.salary

i = Employee("Ruslan", "150000com")
print(f'Мое имя:{i.name}\nЗарплата:{i.salary}')
i.change_name("Islam")
i.display_eployee()
i.display_count()
i.get_total_salary()

class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):  # Инициализатор.
        self.first_name = first_name                      # Атрибут - имя.
        self.second_name = second_name                    # Атрибут - фамилия.
        self.gender = gender                              # Атрибут - пол.
        self.remaining_vacation_days = Employee.vacation_days  # Атриб.отпуска.

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.
class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, date_start, count_days):
        return (f'Начало неоплачиваемого отпуска: {date_start},'
                f' продолжительность: {count_days}.')


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())

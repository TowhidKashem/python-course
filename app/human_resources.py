import dealership as Dealership


class HumanResources(Dealership):
    def __init__(self):
        self.employee_list = {
            'finance': 12,
            'sales': 30,
            'reception': 1,
            'custodian': 2
        }

    def hire_employee(self, department):
        if department in self.employee_list:
            self.employee_list[department] += 1
        else:
            self.employee_list[department] = 1

    def fire_employee(self, department):
        self.employee_list[department] -= 1

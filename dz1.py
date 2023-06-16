class Employee:

    def __init__(self,name,salary,is_good_employee):
        self.name=name
        self.salary=salary
        self.is_good_employee=is_good_employee

    def get_info(self):
        return f'{self.name} зарплата в месяц = {self.salary} хороший сотрудник: {self.is_good_employee}'

baza=[Employee('Kirill',70000,True),Employee('Stepan',85000,False),Employee('Anna',100000,True),Employee('Oleg',90000,True),Employee('Vika',110000,True)]
for i in baza:
    if i=='False':
        baza.remove(Employee)
        break
    print(i.get_info())



    

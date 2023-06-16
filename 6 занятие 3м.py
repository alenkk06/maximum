'''class Year:
    def __init__(self,days,season):
       self.__days=days
       self.__season=season

    def get_days(self):
        return self.__days
    
    def get_season(self):
        return self.__season

    def set_days(self,days):
        if days == 365 or days == 366:
             self.__days=days
        else:
            raise Exception('некорректное зачение')

    def set_season(self,season):
        self.__season=season

year=Year(365,'зима')
year.set_days(500)
print(year.get_days())'''

class Persona:
    def __init__(self,name,age):
       self.__name=name
       self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name (self,name):
        self.__name=name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age<=0:
            raise ValueError('вы ещё не родились!!')
        self.__age=age

    @age.deleter
    def age(self):
        del self.__age

persona=Persona('Alyona',17)

persona.name='Ira'
print(persona.name)

persona.age=20
print(persona.age)

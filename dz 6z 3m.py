class Year:
    def __init__(self,days,season):
       self.__days=days
       self.__season=season

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self,days):
        if not (days==365 or days==366):
            raise ValueError('некорректное значение дней')
        self.__days=days

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self,season):
        self.__season=season
year=Year(365,'лето')
year.days=500
year.season='осень'
print(year.season)
print(year.days)


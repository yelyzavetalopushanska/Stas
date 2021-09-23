# созаем класс (чертеж)
class Dog():
    '''Модель собаки'''
    def __init__(self, name, color, year_of_birth=2000):
        self.name = name
        self.color = color
        self.year_of_birth = year_of_birth

    # метод класса Dog, принадлежит классу Dog
    def voice(self):
        '''Собака лает'''
        print(f"{self.name} лает! Гав")

    def age(self):
        todays_date = int(input(f'Введите год: '))
        if 2020 < todays_date < 2030:
            # оператор return возвращает значение
            return todays_date - self.year_of_birth
        else:
            print(False)




# создание экземпляра класса
my_dog = Dog('dog', 'black')
print(my_dog.name)
print(my_dog.color)
# обращение к методу класса
my_dog.voice()
print(my_dog.age())
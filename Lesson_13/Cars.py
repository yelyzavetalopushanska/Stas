class Car():
    ''' Модель машины '''
    def __init__(self, color, model, engine, odometer=0):
        '''инициализация переменных'''
        self.color = color
        self.model = model
        self.engine = engine
        self.odometer = odometer


    def get_info(self):
        ''' получение полной информации о машине '''
        full_info = f"{self.model} is {self.color}," \
                    f" have {self.engine} " \
                    f"and rage {self.odometer} km"
        return full_info

    def set_odometer(self, odometer):
        if int(odometer) >= 0:
            self.odometer += odometer
        else:
            print("Invalid value")


    def get_fuel(self):
        print("Осталось n литров бензина")


# создаем 2 экземпляра класса Car
ford = Car("red", "Ford focus", "gas")
bmw = Car("black", "BMW X5", "gas", 2000)

# обращаемся к методам экземпляров
print(ford.get_info())
print(bmw.get_info())

# изменение пробега машини через точечную нотацию
ford.odometer = 10_000
print(ford.get_info())

# изменение пробега машини через метод
ford.set_odometer(400)
print(ford.get_info())

# Наследование
class ElectricalCar (Car):
    '''Создание электрокара на основе класса Car'''
    def __init__(self, color, model, odometer=0):
        ''' инициализация переменных '''
        super().__init__(color, model, engine="battery", odometer=odometer)


    def chracge(self):
        print("Мы пока не знаем")


    def get_fuel(self):
        print("Электрокар не имеет бензобака")


tesla = ElectricalCar('gray', 'Tesla')
tesla.get_info()
tesla.chracge()
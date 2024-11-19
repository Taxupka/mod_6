class Vehicle:  # создание класса
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']   # атрибут класса

    def __init__(self, owner, __model, __color, __horse_power): # инициализация объектов класса
        self.owner = owner  # присвоение переменным имен атрибутов
        self.__model = __model
        self.__horse_power = __horse_power
        self.__color = __color


    def get_model(self):    # создание метода get_model
        return f'Модель:{self.__model}' # возвращение атрибута self.__model


    def get_horsepower(self):
        return f'Мощность дигателя:{self.__horse_power}'


    def get_color(self):
        return print(f'Цвет:{self.__color}')


    def print_info(self):   # создание метода print_info
        print(self.get_model()) # печать результата работы метода get_model()
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')



    def set_color(self,new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:  # условие если заданный атрибут в нижнем регистре находится в атрибуте класса
            self.__color = new_color    # присвоение атрибуту значения заданного
        else:
            print(f'Нельзя сменить цвет на {new_color}')    # иначе вывод сообщения



class Sedan(Vehicle):   # создание класса-наследника
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
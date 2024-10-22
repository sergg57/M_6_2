class Vehicle:
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    _COLOR_VARIANTS = ['red', 'blue', 'green', 'yellow']

    def __init__(self, owner, model,  color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self._COLOR_VARIANTS = ['blue', 'red','green', 'black', 'white']

    def get_model(self):
        print(f'Модель: {self.__model}')
        return self.__model

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')
        return self.__engine_power

    def get_color(self):
        print(f'Цвет: {self.__color}')
        return self.__color

    def set_color(self, new_color):
        if new_color.casefold() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на новый: {new_color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()


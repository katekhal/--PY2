if __name__ == "__main__":
    class Pizza:
        """"Базовый класс Pizza"""
        def __init__(self, taste: str, size: float, spicy: bool):
            """
            Создание и подготовка к работе объекта "Пицца"
            :param taste: Вкус пиццы
            :param size: Диаметр пиццы в см
            :param spicy: Острая (да/нет)
            Пример:
            >>> pizza_pepperoni = Pizza("Pepperoni", 25, False)  #Инициализация объекта класса
            """
            if not isinstance(taste, str):
                raise TypeError("Название пиццы должно быть типа str")
            self.taste = taste
            if not isinstance(size, float):
                raise TypeError("Диаметр пиццы должно быть типа float")
            self.size = size
            if not isinstance(spicy, bool):
                raise TypeError("Острота пиццы должна быть типа bool")
            self.spicy = spicy

        @property
        def taste(self) -> str:
            """Возвращает название пиццы"""
            return self.taste

        @property
        def size(self) -> float:
            """Возвращает диаметр пиццы в см"""
            return self.size

        @property
        def spicy(self) -> bool:
            """Возвращает показатель остроты пиццы"""
            if self.spicy:
                how = "Острая"
            else:
                how = "Не острая"
            return how

        def __str__(self):
            """"Реализация магического метода __str__"""
            if self.spicy:
                ostrota = ""
            else:
                ostrota = "не"
            return f"Вы заказали пиццу {self.taste}, диаметром {self.size}, {ostrota}острую"

        def __repr__(self):
            """"Реализация магического метода __repr__"""
            return f"{self.__class__.__name__}(taste={self.taste!r}, size={self.size!r}, spicy={self.spicy!r})"

        def newtoping(self) -> str:
            """
            Меняет топпинг
            >>> pizza1 = Pizza("Pepperoni", 25, False)
            >>> pizza1.newtoping("Margarita")
            """
            ...

    class Dilivery(Pizza):
        """"Дочерний класс доставка"""

        def __init__(self, taste: str, size: float, spicy: bool, slices: int, time: float):
            super().__init__(self, taste, size, spicy)
            if not isinstance(slices, int):
                raise TypeError("Количество кусочков должно быть типа int")
            if slices <= 0:
                raise ValueError("Количество кусочков должно быть положительной величиной")
            self.slices = slices

            if not isinstance(time, float):
                raise TypeError("Время доставки должно быть типа float")
            if time <= 0:
                raise ValueError("Время доставки должно быть положительной величиной")
            self.time = time

        def __str__(self) -> str:
            """"Перегрузка метода"""
            if self.spicy:
                ostrota = ""
            else:
                ostrota = "не"
            return f"Вы заказали пиццу {self.taste}, диаметром {self.size}, {ostrota}острую. " \
                   f"Пицца разрезана на {self.slices} кусочков, приблизительное время доставки {self.time}"

        def __repr__(self):
            """"Перегрузка магического метода __repr__"""
            return f"{self.__class__.__name__}(taste={self.taste!r}, size={self.size!r}, spicy={self.spicy!r}, slices={self.slices!r}, time={self.time!r}) "

        @property
        def slices(self) -> int:
            """"Возвращает время доставки."""
            return self.slices

        @slices.setter
        def population(self, how_many: int) -> None:
            """"Устанавливает количество кусочков пиццы"""
            if isinstance(how_many, int):
                if how_many > 0:
                    self.slices = how_many
                else:
                    raise ValueError(f'Такое число кусочков невозможно: {how_many!r}')
            else:
                raise TypeError(f'Неверный формат: {how_many!r}')
    pass

import doctest


class Backpack:
    def __init__(self, amount_of_books: int, mass: float):
        """
        Создание и подготовка к работе объекта "Рюкзак"
        :param amount_of_books: Сколько книг посместится в рюкзак
        :param mass: Сколько весит рюкзак
        Примеры:
        >>> backpack = Backpack(5, 1000)  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_books, (int)):
            raise TypeError("Косичество вмещающихся книг в рюкзак должно быть типа int")
        if mass <= 0:
            raise ValueError("Масса рюкзака должна быть положительным числом")
        self.amount_of_books = amount_of_books

        if not isinstance(mass, (int, float)):
            raise TypeError("Масса рюкзака должна быть int или float")
        if amount_of_books < 0:
            raise ValueError('Количество книг не может быть отрицательным числом')
        self.mass = mass

    def is_empty(self) -> bool:
        """
        Функция которая проверяет является ли рюкзак пустым
        :return: Является ли рюкзак пустым
        Примеры:
        >>> backpack = Backpack(5, 1000)
        >>> backpack.is_empty()
        """
        ...

    def add_book(self, addbook: int) -> None:
        """
        Добавление книг в рюкзак.
        :param addbook: Количество добавленных книг
        :raise ValueError: Если количество добавляемых книг отрицательно, вызываем ошибку
        >>> backpack = Backpack(5, 1000)
        >>> backpack.add_book(1)
        """
        if not isinstance(addbook, (int)):
            raise TypeError("Количество книг должно быть типа int")
        if addbook < 0:
            raise ValueError("Количество добавляемых книг должно быть положительным числом")
        ...

    def remove_book(self, rem_book: int) -> None:
        """
        Извлечение воды из стакана.
        :param rem_book: Количество извлекаемых книг
        :raise ValueError: Если количество извлекаемых книг отрицательно, вызываем ошибку
        Примеры:
        >>> rem_book = Backpack(5, 1000)
        >>> rem_book.remove_book(2)
        """
        ...

class Instagram:
    def __init__(self, amount_of_followers: int, amount_of_followings: int, amount_of_pics: int):
        """
        Создание и подготовка к работе объекта "Instagram"
        :param amount_of_followers: Сколько аккаунтов в подписчиках
        :param amount_of_followings: Сколько аккаунтов в подписках
        :param amount_of_pics: Количество фото в профиле
        Примеры:
        >>> backpack = Instagram(100, 200, 10)  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_followers, (int)):
            raise TypeError("Косичество подписчиков должно быть типа int")
        if not isinstance(amount_of_followings, (int)):
            raise TypeError("Косичество подписок должно быть типа int")
        if not isinstance(amount_of_pics, (int)):
            raise TypeError("Косичество фото в профиле должно быть типа int")
        if amount_of_followers < 0:
            raise ValueError('Параметр "amount_of_followers" должен положительным')
        if amount_of_followings < 0:
            raise ValueError('Параметр "amount_of_followings" должен положительным')
        if amount_of_pics < 0:
            raise ValueError('Параметр "amount_of_pics" должен положительным')
        self.amount_of_followers = amount_of_followers
        self.amount_of_followings = amount_of_followings
        self.amount_of_pics = amount_of_pics
    def is_equal(self) -> int:
        """
        Функция которая проверяет количество взимных подписок
        :return: Количество "пар"
        Примеры:
        >>> account = Instagram(100, 100, 3)
        >>> account.is_equal()
        """
        ...

    def annul_acc(self) -> None:
        """
        Очистка аккаунта
        >>> acc = Instagram(100, 200, 1000)
        >>> acc.annul_acc()
        """
        amount_of_followers = None
        amount_of_followings = None
        amount_of_pics = None
        ...

class Phone:
    """
        Описание модели телефона.
        """

    def __init__(self, brand: str, series: str) -> None:
        """
        Создание и подготовка к работе объекта "Телефон"
        :param brand: Марка телефона
        :param series: Модель телефона
        Пример:
        >>> phone = Phone("Iphone", "20")  # инициализация экземпляра класса
        """

        self.brand = brand
        self.series = series

    def display_size(self, length: float, width: float) -> float:
        """
        Метод, который определяет размер дисплея
        :param length: Длина дисплея (в милиметрах)
        :param width: Ширина дисплея (в милиметрах)
        :return: Длина и ширина (в милиметрах)

        Пример:
        >>> phone = Phone("Iphone", "20")
        >>> phone.display_size(150.9, 75.7)
        """
        if not isinstance((length and width), (float, int)):
            raise TypeError("Длина и ширина должны быть типа int или float ")
        if length and width <= 0:
            raise ValueError("Длина и ширина должны быть больше нуля")
        ...

    def get_year(self, year: int) -> None:
        """
        Определяет год выпуска телефона
        :param year: Год выпуска
        Пример:
        >>> phone = Phone("Iphone", "20")
        >>> phone.get_year(2029)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_directory = os.path.abspath('../src/items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f'Item{self.name, self.price, self.quantity}'

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

        return None

    @property
    def name(self):
        """Получает название товара
        :return: Название товара"""
        return self.__name

    @name.setter
    def name(self, value):
        """проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезает строку (оставить первые 10 символов)."""
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, path=file_directory):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        если файл csv отсутствует то вызывается исключение"""

        try:
            if not os.path.exists(path):
                raise FileNotFoundError('Отсутствует файл items.csv')
            cls.all = []
            with open(path) as file:
                reader = csv.DictReader(file, delimiter=',')
                for line in reader:
                    if set(line) != {'name', 'price', 'quantity'}:
                        raise InstantiateCSVError()
                    cls(line['name'], float(line['price']), int(line['quantity']))

        except FileNotFoundError:
            raise
        except Exception:
            raise InstantiateCSVError()

    @staticmethod
    def string_to_number(value):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(value))


class InstantiateCSVError(Exception):
    """
    Исключение всплывающее при ошибке чтения файла.
    """

    def __init__(self, message="Файл item.csv поврежден"):
        super().__init__(message)
        self.message = message

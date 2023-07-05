from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создает экземпляр класса Phone.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f'Phone{self.name, self.price, self.quantity, self.number_of_sim}'

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        """возвращает кол-во поддерживаемых сим"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Если количество сим равно или меньше 0 то выдает ошибку"""
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value

    def __add__(self, other) -> int:
        """
        Результатом сложения будет суммарное количество товара.
        other: Другой объект для сложения (экземпляр класса Phone или Item).
        return: суммарное количество товара.
        TypeError: если other не является экземпляром класса Phone или Item будет ошибка.
        """
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать количество телефонов с другим типом данных")

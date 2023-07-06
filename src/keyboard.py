from src.item import Item


class MixinLang:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
            return self
        else:
            self.__language = 'RU'
            return self


class KeyBoard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)

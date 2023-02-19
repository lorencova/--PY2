import doctest

some_shit = {
    "Clostridium tetani": {"domain": "прокариоты",               # царство
                           "phylum": "настоящие бактерии",       # подцарство
                           "genus": "клостридии",                # род
                           "species": "Столбнячная палочка",     # вид
                           "sex_process": "конъюгация"},         # половой процесс

    "Nostoc pruniforme": {"domain": "прокариоты",
                          "phylum": "цианобактерии",
                          "genus": "носток",
                          "species": "Носток сливообразный",
                          "sex_process": "отсутствует"},

    "Bordetella pertussis": {"domain": "прокариоты",
                             "phylum": "настоящие бактерии",
                             "genus": "бордетеллы",
                             "species": "Бактерия Борде — Жангу (палочка коклюша)",
                             "sex_process": "конъюгация"},

    "Protosiphon botryoides": {"domain": "прокариоты",
                           "phylum": "цианобактерии",
                           "genus": "протосифон",
                           "species": "Протосифон ботриоидный ",
                           "sex_process": "отсутствует"}
}                                                                  # словарь со всеми прокариотами (может быть больше)

#_______________________________________________________________________________________________________________________________________

class Prokaryote:

    def __init__(self, species_latin: str, num_delenii: int):
        """
        Базовый класс прокариоты.
        :param species_latin: название вида на латинском
        :param num_delenii: количество делений 1 прокариота
        Пример:
        >>> prokaryote1 = Prokaryote("Nostoc pruniforme", 3)
        """
        if some_shit.get(species_latin) != None:
            self._species_latin = species_latin
        else:
            raise NameError(f'error: прокариота {species_latin!r} не существует или допущена ошибка')

        if isinstance(num_delenii, int):
            if num_delenii > 0:
                self.num_delenii = num_delenii
            else:
                raise ValueError(f'error: num_delenii must be a positive number: {num_delenii!r}')
        else:
            raise TypeError(f'error: number of pages must be int type: {num_delenii!r}')

    def __str__(self) -> str:
        """
        Магический метод __str__
        :return: строку для чтения
        Пример:
        >>> prokaryote1 = Prokaryote("Nostoc pruniforme", 9)
        >>> prokaryote1.__str__()
        "Носток сливообразный (лат. Nostoc pruniforme) относится к подцарству 'цианобактерии' царства 'прокариоты'"
        """
        a = some_shit[self._species_latin]["domain"]
        b = some_shit[self._species_latin]["phylum"]
        c = some_shit[self._species_latin]["species"]
        return f"{c} (лат. {self._species_latin}) относится к подцарству '{b}' царства '{a}'"

    def __repr__(self) -> str:
        """
        Магический метод __repr__
        :return: строку, показывающую, как может быть инициализирован экземпляр
        Пример:
        >>> prokaryote1 = Prokaryote("Nostoc pruniforme", 9)
        >>> prokaryote1.__repr__()
        "Prokaryote(species_latin = 'Nostoc pruniforme')"
        """
        return f"{self.__class__.__name__}(species_latin = {self._species_latin!r})"

    def delenie(self):
        """
        Функция, иллюстрирующая геометрическую прогрессию
        :return: количество прокариотов после num_delenii делений
        Пример:
        >>> prokaryote1 = Prokaryote("Nostoc pruniforme", 7)
        >>> prokaryote1.delenie()
        'после 7 делений получилось 128 прокариот'
        """
        num_prokaryotes = 2 ** self.num_delenii
        return f"после {self.num_delenii!r} делений получилось {num_prokaryotes} прокариот"

    @property
    def species_latin(self):
        return self._species_latin # делаем атрибут _species_latin только для чтения, объявив getter

#_______________________________________________________________________________________________________________________________________

class Bacteria(Prokaryote): # нследуемся от Prokaryote

    def __init__(self, species_latin: str, num_delenii: int):
        """
        Дочерний класс настоящие бактерии.
        :param name: название вида на латинском
        :param sequence: количество делений 1 бактерии
        Пример:
        >>> prokaryote1 = Bacteria("Clostridium tetani", 7)
        """
        super().__init__(species_latin, num_delenii)

    def delenie(self):
        """
        Функция, иллюстрирующая геометрическую прогрессию
        Перегружен, так как здесь делятся уже конкретно нстоящие бактерии, а не в общем прокариоты
        :return: количество настоящих бактерий после num_delenii делений
        Пример:
        >>> prokaryote1 = Bacteria("Clostridium tetani", 5)
        >>> prokaryote1.delenie()
        'после 5 делений получилось 32 настоящих бактерий'
        """
        num_prokaryotes = 2 ** self.num_delenii
        return f"после {self.num_delenii!r} делений получилось {num_prokaryotes} настоящих бактерий"

    def __str__(self) -> str:
        """
        Магический метод __str__
        Перегружен из-за дополнения информации о половом процессе
        :return: строку для чтения
        Пример:
        >>> prokaryote2 = Bacteria("Clostridium tetani", 84)
        >>> prokaryote2.__str__()
        'Столбнячная палочка (лат. Clostridium tetani). Половой процесс - конъюгация'
        """
        a = some_shit[self._species_latin]["domain"]
        b = some_shit[self._species_latin]["phylum"]
        c = some_shit[self._species_latin]["species"]
        d = some_shit[self._species_latin]["sex_process"]
        return f"{c} (лат. {self._species_latin}). Половой процесс - {d}"

#_______________________________________________________________________________________________________________________________________

class Cyanobacteria(Bacteria): # наследуемся от Bacteria
    """
    Дочерний класс Цианобактерии.
    :param name: название вида на латинском
    :param sequence: количество делений 1 цианобактерии
    Пример:
    >>> prokaryote1 = Cyanobacteria("Nostoc pruniforme", 8)
    """
    def delenie(self):
        """
        Функция, иллюстрирующая геометрическую прогрессию
        Перегружен, так как здесь делятся цианобактерии
        :return: количество цианобактерий после num_delenii делений
        Пример:
        >>> prokaryote3 = Cyanobacteria("Nostoc pruniforme", 7)
        >>> prokaryote3.delenie()
        'после 7 делений получилось 128 цианобактерий'
        """
        num_prokaryotes = 2 ** self.num_delenii
        return f"после {self.num_delenii!r} делений получилось {num_prokaryotes} цианобактерий"

#_______________________________________________________________________________________________________________________________________


prokaryote1 = Prokaryote("Bordetella pertussis", 13)
print(prokaryote1.num_delenii)
print(prokaryote1.__str__())
print(prokaryote1.delenie())
print(prokaryote1.species_latin)
print(prokaryote1.__repr__(), "\n")

prokaryote2 = Bacteria("Bordetella pertussis", 84)
print(prokaryote2.num_delenii)
print(prokaryote2.__str__())
print(prokaryote2.delenie())
print(prokaryote2.species_latin)
print(prokaryote2.__repr__(), "\n")

prokaryote3 = Cyanobacteria("Protosiphon botryoides", 3)
print(prokaryote3.num_delenii)
print(prokaryote3.__str__())
print(prokaryote3.delenie())
print(prokaryote3.species_latin)
print(prokaryote3.__repr__(), "\n")


# prokaryote1.species_latin = "что такое прокариоты???"
# print(prokaryote1.species_latin) # вызов getter свойства, проверка его работы
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


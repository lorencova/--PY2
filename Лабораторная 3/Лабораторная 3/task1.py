class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name # инициализируем защищенные атрибуты
        self._author = author

    def __str__(self) -> str:
        return f'Книга "{self._name}". Автор: {self._author}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r})"

    @property
    def name(self):
        return self._name # внутри класса обращаемся к защищенному атрибуту

    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self._pages = pages
            else:
                raise ValueError(f'error: pages must be a positive number: {pages!r}')
        else:
            raise TypeError(f'error: number of pages must be int type: {pages!r}')

    @property
    def pages(self):
        return self._pages

    def __str__(self) -> str:
        return f'Книга "{self._name}" - бумажная. Автор: {self._author}. Количество страниц: {self._pages}' # перегрузка метода __str__

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r}, pages = {self._pages!r})" # перегрузка метода __repr__

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self._duration = duration

            else:
                raise ValueError(f'error: duration must be a positive number: {duration!r}')
        else:
            raise TypeError(f'error: duration must be a float type: {duration!r}')

    @property
    def duration(self):
        return self._duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r}, duration = {self._duration!r})" # перегрузка метода __repr__

#____________________________________________________________________________________________________________________________________________________________

book = Book("Элетротехника", "И. И. Иванов")
print("1.", book)
print("2.", book.__repr__(), "\n")

book1 = PaperBook("Нормальная анатомия человека", "И. В. Гайворонский", 669)
print("3.", book1)

book2 = PaperBook("Исповедь маски", "Ю. Мисима", 200)
print("4.", book2)
print("5.", book2.__repr__(), "\n")

# book2.name = "Незнайка на луне"
# print(book2.name) # вызов getter свойства, проверка его работы

# book2.pages = 201
# print(book2.pages)

book3 = AudioBook("Преступление и наказание", "Ф. М. Достоевский", 2.3993)
print("6.", book3) # наследует метод __str__

book4 = AudioBook("Морфий", "М. А. Булгаков", 0.8)
print("7.", book4.__repr__())



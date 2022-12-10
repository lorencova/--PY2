# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import random
def random_gene(length):
    letters = 'ACTG'
    rand_gene = ''.join(random.choice(letters) for i in range(length))
    return rand_gene
# добавила сделанне мною ранее задание для основного курса в универе
class Gene:
    def __init__(self, name, sequence):
        """
        Подготовка к работе объекта "Ген"
        :param name: назвавание гена
        :param sequence: последовательность
        Пример:
        >>> short_dna = Gene("partofKRT16", "ACGTA") # иницилизация экземпляра класса
        """
        self.name = name
        if sequence.isupper() == False:
            raise TypeError("впишите последовательность в верхнем регистре!")
        self.sequence = sequence
    def transcribe(self):
        """
        Функция, которая выводит последовавательность комплементарную данной
        :return: комплементарная данной последовательности
        Пример:
        >>> short_dna = Gene("part of KRT16", "ACGTA")
        >>> short_dna.transcribe()
        'TGCAT'
        """
        dna = self.sequence.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        dna = dna.upper()
        return dna
    def translate(self):
        """
        Трансляция полученной последовательности:
        :return: РНК в результате трансляции
        Пример:
        >>> short_dna = Gene("part of KRT16", "ACGTA")
        >>> short_dna.translate()
        'ACGUA'
        """
        rna = self.transcribe().replace('A', 'u').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        rna = rna.upper()
        return rna
    def prc_adenyne_thymine(self):
        """
        Подсчет соотношения аденина и тимина в последовавательности, комплементарной данной
        :return: процентное содержание аденина и тимина
        Пример:
        >>> short_dna = Gene("part of KRT16", "ACGTA")
        >>> short_dna.prc_adenyne_thymine()
        60.0
        """
        short_dna_lenght = len(self.transcribe())
        adenyne, thymine = 'A', 'T'
        sum_a, sum_t = self.transcribe().count('A'), self.transcribe().count('T')
        result = (sum_a + sum_t) / short_dna_lenght * 100
        return result

short_dna = Gene('random gene', random_gene(37))
print(short_dna.name, ":", short_dna.sequence, "\n")
print("последоваательность, комплементарная", short_dna.name, ":\n", short_dna.transcribe())
print("РНК в результате трансляции", short_dna.name, ":\n", short_dna.translate())
print("соотношение аденина и тимина в последоваательности, комплементарной", short_dna.name, ":\n", short_dna.prc_adenyne_thymine(), "%")

#_______________________________________________________________________________________

class Book:
    def __init__(self, name, num_of_pages, num_of_str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name: назвавание книги
        :param num_of_pages: количество страниц
        :param num_of_str: примерное количество строк на одной странице
        Примеры:
        >>> for_gadanie = Book("Триумфальная арка", 639, 34) # иницилизация экземпляра класса
        """
        self.name = name
        if not isinstance(num_of_pages, int):
            raise TypeError("у книги должно быть целое число страниц")
        if num_of_pages <= 0:
            raise ValueError("у книги есть страницы")
        self.num_of_pages = num_of_pages
        if not isinstance(num_of_str, int):
            raise TypeError
        if num_of_str <= 0:
            raise ValueError("хотя бы одна строка у книги должна быть")
        self.num_of_str = num_of_str
    def page_for_gadanie(self):
        """
        Функция, которя выбирает случайную страницу
        :return: рандомный номер страницы книги
        Примеры:
        >>> for_gadanie = Book("Триумфальная арка", 639, 34)
        >>> for_gadanie.page_for_gadanie()
        """
        ...
    def direction(self):
        """
        Функция, которая выбирет, сверху отсчитывать строки или снизу, в зависимости от четности/нечетности символов в названии
        :return: "сверху", если четное число символов в нзвании и "снизу", если нечетное
        Примеры:
        >>> for_gadanie = Book("Триумфальная арка", 639, 34)
        >>> for_gadanie.direction()
        """
        ...
    def str_for_gadanie(self):
        """
        Если сумма всех страниц и примерного количества строк на одной странице - четное число, то выбирается рандомная четная строка
        И наоборот, если сумма - нечетное число, то выбирается рандомная нечетная строка
        :return: номер строки
        Примеры:
        >>> for_gadanie = Book("Триумфальная арка", 639, 34)
        >>> for_gadanie.str_for_gadanie()
        """
        ...

#_______________________________________________________________________________________

class Doge:
    def __init__(self, name, sex, age):
        """
        Создание и подготовка к работе объекта "Собачка"
        :param name: кличка
        :param sex: пол
        :param age: возраст
        Примеры:
        >>> dog = Doge("Тося", "ж", 5) # иницилизация экземпляра класса
        """
        self.name = name
        self.sex = sex
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def get_description(self):
        """
        Функция, которая выводит на экран описание собачки: ее кличку, породу и возраст
        :return: текстовое описание собачки

        Примеры:
        >>> dog = Doge("Тося", "ж", 5)
        >>> dog.get_description()
        """
        ...
    def sit(self):
        """
        Собачка садится по команде
        :return: текст "*кличка* сел/села"

        Примеры:
        >>> dog = Doge("Тося", "ж", 5)
        >>> dog.sit()
        """
        ...
    def jump(self):
        """
        Собчка делает прыжок по команде
        :return: текст "прыжок!"

        Примеры:
        >>> dog = Doge("Тося", "ж", 5)
        >>> dog.jump()
        """
        ...

#_______________________________________________________________________________________

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod() #тестирование примеров, которые находятся в документации

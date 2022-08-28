'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

class Sklad:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.device = {'Название устройства:': self.name, 'Цена, ед:': self.price, 'Количество, шт': self.quantity}

    def vvod(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            device = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            self.device.update(device)
            print(self.device)
        except ValueError:
            print('Ошибка ввода!')

class Printer(Sklad):
    pass

class Scanner(Sklad):
    pass

class Xerox(Sklad):
    pass

a = Printer('Epson', 4500, 20)
b = Scanner('Brother', 1000, 30)
c = Xerox('Xerox', 6000, 10)
a.vvod()
b.vvod()
c.vvod()
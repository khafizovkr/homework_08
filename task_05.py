# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
from abc import ABC, abstractmethod


class NumberCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, warehouse_volume):
        self.warehouse_volume = warehouse_volume
        self.warehouse_items = []
        self.remaining_volume = warehouse_volume

    def add_equipment(self, equipment):
        self.warehouse_items.append(equipment)
        self.remaining_volume -= equipment.items_volume
        if self.remaining_volume < 0:
            self.warehouse_items.pop()
            self.remaining_volume += equipment.items_volume
            print(f'Склад полон. Товар не принят. Осталось {self.remaining_volume} места для хранения.')
        elif self.remaining_volume < 0.1 * self.warehouse_volume:
            print(f'Место на складе заканчивается. {equipment} принят на склад.\n'
                  f'Осталось {self.remaining_volume} места для хранения.\n')
        else:
            print(f'{equipment} принят на склад.\n'
                  f'Осталось {self.remaining_volume} места для хранения.\n')

    def remove_equipment(self, destination, item_name, amount):
        for el in self.warehouse_items:
            if item_name in el.values():
                el['Количество устройств'] -= amount
                if el['Количество устройств'] == 0:
                    self.warehouse_items.remove(el)
                elif el['Количество устройств'] < 0:
                    print('Недостаточно товара на складе.')
                self.remaining_volume -= el['Количество устройств'] * el['Объем устройства']
                print(f'{amount} {el.discr()}ов {item_name} переданы в подразделение {destination}')

    def inventory_check(self):
        print('\nИнвентаризация')
        equipment_volume = 0
        for el in self.warehouse_items:
            print(el)
            equipment_volume += el['Количество устройств'] * el['Объем устройства']
        print(f'Объем техники {equipment_volume}\n')


class OfficeEquipment(ABC):
    def __init__(self, item_name, amount, unit_volume):
        self.item_name = item_name
        self.amount = amount
        if type(amount) != int:
            raise NumberCheck('Введите число')
        self.unit_volume = unit_volume
        if type(unit_volume) != int and type(unit_volume) != float:
            raise NumberCheck('Введите число')
        self.items_volume = unit_volume * amount
        self.item_dict = {'Устройство': self.item_name,
                          'Количество устройств': self.amount,
                          'Объем устройства': self.unit_volume}

    def __str__(self):
        return str(self.item_dict)

    def __mul__(self, other):
        return self.unit_volume * self.amount

    def values(self):
        return self.__dict__.values()

    def __setitem__(self, key, value):
        self.item_dict[key] = value

    def __getitem__(self, key):
        return self.item_dict[key]

    @abstractmethod
    def discr(self):
        return ' '


class Printer(OfficeEquipment):
    def action(self):
        return 'Печать'

    def discr(self):
        return 'Принтер'


class Scanner(OfficeEquipment):
    def action(self):
        return 'Скан'

    def discr(self):
        return 'Сканер'


class CopyMachine(OfficeEquipment):
    def action(self):
        return 'Копия'

    def discr(self):
        return 'Копир'

wh = Warehouse(500)
pr = Printer('HP', 500, 0.03)
sc = Scanner('Canon', 1000, 0.01)
cm = CopyMachine('Kyocera', 800, 0.2)
wh.add_equipment(pr)
wh.add_equipment(sc)
wh.inventory_check()
wh.add_equipment(cm)
wh.inventory_check()
wh.remove_equipment('Офис 101', 'Canon', 100)
wh.inventory_check()

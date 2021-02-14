# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
class NumberCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, warehouse_volume):
        self.warehouse_volume = warehouse_volume
        self.warehouse_items = []
        self.remaining_volume = warehouse_volume

    def add_equipment(self, item_name, amount, unit_volume):
        self.warehouse_items.append(OfficeEquipment(item_name, amount, unit_volume))
        self.remaining_volume -= OfficeEquipment(item_name, amount, unit_volume).items_volume
        if self.remaining_volume < 0:
            self.warehouse_items.pop()
            self.remaining_volume += OfficeEquipment(item_name, amount, unit_volume).items_volume
            print(f'Склад полон. Товар не принят. Осталось {self.remaining_volume} места для хранения.')
        elif self.remaining_volume < 0.1 * self.warehouse_volume:
            print(f'Место на складе заканчивается. {OfficeEquipment(item_name, amount, unit_volume)} принят на склад.\n'
                  f'Осталось {self.remaining_volume} места для хранения.\n')
        else:
            print(f'{OfficeEquipment(item_name, amount, unit_volume)} принят на склад.\n'
                  f'Осталось {self.remaining_volume} места для хранения.\n')

    def remove_equipment(self, destination, item_name, amount):
        for el in self.warehouse_items:
            # print(el)
            if item_name in el.values():
                el['Количество устройств'] -= amount
                if el['Количество устройств'] == 0:
                    self.warehouse_items.remove(el)
                elif el['Количество устройств'] < 0:
                    print('Недостаточно товара на складе.')
                self.remaining_volume -= el['Количество устройств'] * el['Объем устройства']
                print(f'{amount} {item_name} переданы в подразделение {destination}')

    def inventory_check(self):
        print('\nИнвентаризация')
        equipment_volume = 0
        for el in self.warehouse_items:
            print(el)
            equipment_volume += el['Количество устройств'] * el['Объем устройства']
        print(f'Объем техники {equipment_volume}\n')


class OfficeEquipment:
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


class Printer(OfficeEquipment):
    def action(self):
        return 'Печать'


class Scanner(OfficeEquipment):
    def action(self):
        return 'Скан'


class CopyMachine(OfficeEquipment):
    def action(self):
        return 'Копия'


wh = Warehouse(500)
pr = Printer('HP', 500, 0.03)
sc = Scanner('Canon', 1000, 0.01)
cm = CopyMachine('Kyocera', 800, 0.2)
wh.add_equipment(pr.item_name, pr.amount, pr.unit_volume)
wh.add_equipment(sc.item_name, sc.amount, sc.unit_volume)
wh.inventory_check()
wh.add_equipment(cm.item_name, cm.amount, cm.unit_volume)
wh.inventory_check()
wh.remove_equipment('Офис 101', 'Canon', 100)
wh.inventory_check()

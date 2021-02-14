# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
class WarehouseFull(Exception):
    def __init__(self, txt):
        self.txt = txt


class NotEnoughItems(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, warehouse_volume):
        self.warehouse_volume = warehouse_volume
        self.equipment_volume = 0
        self.warehouse_items = []
        self.remaining_volume = warehouse_volume

    def add_equipment(self, item_name, amount, unit_volume):
        self.warehouse_items.append(OfficeEquipment(item_name, amount, unit_volume))
        self.remaining_volume -= OfficeEquipment(item_name, amount, unit_volume).items_volume
        if self.remaining_volume < 0.1 * self.warehouse_volume:
            print(f'Место на складе заканчивается. Осталось {self.remaining_volume} места для хранения.')
        elif self.remaining_volume < 0:
            self.warehouse_items.pop()
            self.remaining_volume += OfficeEquipment(item_name, amount, unit_volume).items_volume
            raise WarehouseFull(f'Склад полон. Товар не принят. Осталось {self.remaining_volume} места для хранения.')
        print(f'{OfficeEquipment(item_name, amount, unit_volume)} принят на склад.\n '
              f'Осталось {self.remaining_volume} места для хранения.\n')

    def remove_equipment(self, destination, item_name, amount):
        for el in self.warehouse_items:
            print(type(el))
            if item_name in el.__iter__.values():
                el['Количество устройств'] -= amount
                if el['Количество устройств'] == 0:
                    self.warehouse_items.remove(el)
                elif el['Количество устройств'] < 0:
                    raise NotEnoughItems('Недостаточно товара на складе.')
                self.remaining_volume -= el['Количество устройств'] * el['Объем устройства']
                print(f'{amount} {item_name} переданы в подразделение {destination}')

    def inventory_check(self):
        for el in self.warehouse_items:
            print(el)
            self.equipment_volume += el['Количество устройств'] * el['Объем устройства']
        print(f'Объем техники {self.equipment_volume}\n')


class OfficeEquipment:
    def __init__(self, item_name, amount, unit_volume, *values):
        self.item_name = item_name
        self.amount = amount
        self.unit_volume = unit_volume
        self.items_volume = unit_volume * amount
        self.item_dict = {'Устройство': self.item_name,
                          'Количество устройств': self.amount,
                          'Объем устройства': self.unit_volume}
        self.some_sequence = values

    def __str__(self):
        return str(self.item_dict)

    def __getitem__(self, index):
        return self

    def __mul__(self, other):
        return self.unit_volume * self.amount

    def __iter__(self):
        for values in self.some_sequence:
            yield values


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
pr = Printer('HP', 500, 0.01)
sc = Scanner('Samsung', 1000, 0.005)
cm = CopyMachine('Kyocera', 800, 0.5)
wh.add_equipment(pr.item_name, pr.amount, pr.unit_volume)
wh.add_equipment(sc.item_name, sc.amount, sc.unit_volume)
wh.inventory_check()
wh.add_equipment(cm.item_name, cm.amount, cm.unit_volume)
wh.inventory_check()
wh.remove_equipment('Офис 101', 'Samsung', 100)
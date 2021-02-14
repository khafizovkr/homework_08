# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import calendar


class WrongMonth(Exception):
    def __init__(self, txt):
        self.txt = txt


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        for number in date.split('-'):
            print(int(number), end=' ')
        else:
            print('\n')

    @staticmethod
    def date_for_validation(date):
        date_val = [int(number) for number in date.split('-')]
        try:
            if date_val[0] not in range(1, calendar.monthrange(date_val[2], date_val[1])[1] + 1):
                print(f'{date} not valid: bad day number {date_val[0]}; must be 1-{calendar.monthrange(date_val[2], date_val[1])[1]}')
            else:
                print(f'{date} is valid')
        except calendar.IllegalMonthError:
            print(f'{date} not valid: bad month number {date_val[1]}; must be 1-12')


Data.get_date('30-06-1994')
Data.date_for_validation('30-11-1994')
Data.date_for_validation('31-11-2004')
Data.date_for_validation('12-13-2004')
Data.date_for_validation('29-02-2006')
Data.date_for_validation('29-02-2008')

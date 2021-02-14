# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


divident = int(input('Введите делимое '))
try:
    divider = int(input('Введите делитель '))
    if divider == 0:
        raise MyError('Деление на ноль')
except MyError as err:
    print(err)
else:
    print(divident / divider)

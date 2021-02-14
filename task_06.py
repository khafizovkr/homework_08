# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.
#OVERRIDE DICT
def dict(obj):
    if isinstance(obj,Foo):
        return f.__dict__
    else:
        return obj

#YOUR CLASS
class Foo:
    def __init__(self):
        self.var1 = 'one'
        self.var2 = 'two'
        self.var3 = 'three'
        self.var4 = 'four'

#TEST
f = Foo()
exampleDict = {1:"one",2:"two",3:"three",4:"four"}

sam1 = dict(f) #GET THE OBJECT BACK AS DICTIONARY
sam2 = dict(exampleDict) #A DICTIONARY OBJECT

#PRINT
print(sam1)
print(sam2)
print({1:"one",2:"two",3:"three",4:"four"})
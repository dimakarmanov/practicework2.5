from random import randrange
list = []
for i in range(10):
    number = randrange(0, 100, 2)
    list.append(number)
print(sorted(list))
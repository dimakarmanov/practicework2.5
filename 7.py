import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
r = int(input("Введите радиус: "))
belong_to_circle = math.sqrt(x**2 + y**2)
if belong_to_circle <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
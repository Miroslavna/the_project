from math import sqrt
u = 0
d = 0
l = 0
r = 0
while True:
    str = input("Введите направление и количество шагов через пробел: \n (пример: u 10)")
    var = str.split(" ")
    if len(var) >= 2:
        dist = int(var[1])
    else:
        dist = 0
    if var[0] == 'u':
        u = u + dist
    if var[0] == 'd':
        d = d + dist
    if var[0] == 'l':
        l = l + dist
    if var[0] == 'r':
        r = r + dist
    elif var[0] == 'q':
        break
x = u - d
y = l - r
z = x**2 + y**2 
z = sqrt(z)
print(z)
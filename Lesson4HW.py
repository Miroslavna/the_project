from re import A


a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
a_1 = a and b and c and "Нет нулевых значений"
print(a_1)
a_2 = a or b or c or "Введены все нули"
print(a_2)
if a > b + c: print(a - b - c)
if a < b + c: print(b + c - a)
if a > 50 and b > a or c > a: print("Вася")
if a > 5 or b == 7 and c == 7: print("Петя")
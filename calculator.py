height = float(input("Введите ваш рост, см: "))
weight = float(input("Введите ваш вес, кг: "))
bmi = weight / (height/100) **2
print(f"Ваш ИМТ = <{round(bmi,1)}>")
print('18' + '=' * (int(bmi)-18) + '|' + '=' * (30 - int(bmi)))
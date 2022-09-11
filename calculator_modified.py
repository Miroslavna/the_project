height = float(input("Введите ваш рост, см: ")) 
weight = float(input("Введите ваш вес, кг: "))
gender = input("Укажите ваш пол (м если вы мужчина, ж если женщина): ")
age = int(input("Укажите ваш возраст: "))
bmi = weight / (height/100) **2
print(f"Ваш ИМТ = <{round(bmi,1)}>")
print('15' + '=' * (int(bmi)-18) + '|' + '=' * (40 - int(bmi)))
# Рачет ИМТ для мужчин с учетом возраста
if gender == 'м' and bmi <= 20 and age <= 40:
    print("Низкий ИМТ")
elif gender == 'м' and bmi > 20 and bmi <= 25 and age <= 40:
    print("Норма")
elif gender == 'м' and bmi > 25 and bmi <= 30 and age <= 40:
    print("Высокий ИМТ")
elif gender == 'м' and bmi > 30 and bmi <= 40 and age <= 40:
    print("Ожирение 1-2 степени. Необходима консультация специалиста.")
elif gender == 'м' and bmi > 40 and age < 40:
    print("Ожирение 3 степени. Необходима срочная консультация специалиста.")
elif gender == 'м' and bmi <= 20 and age > 40:
    print("Критически низкий ИМТ. Необходима консультация специалиста.")
elif gender == 'м' and bmi > 22 and bmi <= 28 and age > 40:
    print("Норма")
elif gender == 'м' and bmi > 28 and bmi <= 32 and age > 40:
    print("Высокий ИМТ")
elif gender == 'м' and bmi > 32 and bmi <= 40 and age > 40:
    print("Ожирение 1-2 степени. Необходима консультация специалиста.")
elif gender == 'м' and bmi > 40 and bmi < 50 and age > 40:
    print("Ожирение 3 степени. Необходима срочная консультация специалиста.")
# Рачет ИМТ для женщин с учетом возраста
if gender == 'ж' and bmi <= 19 and age <= 40:
    print("Низкий ИМТ")
elif gender == "ж" and bmi > 19 and bmi <= 24 and age <= 40:
    print("Норма")
elif gender == "ж" and bmi > 24 and bmi <= 30 and age <= 40:
    print("Высокий ИМТ.")
elif gender == "ж" and bmi > 30 and bmi <= 40 and age <= 40:
    print("Ожирение 1-2 степени. Необходима консультация специалиста.")
elif gender == "ж" and bmi > 40 and age <= 40:
    print("Ожирение 3 степени. Необходима срочная консультация специалиста.")
elif gender == 'ж' and bmi <= 19 and age > 40:
    print("Критически низкий ИМТ. Необходима срочная консультация специалиста.")
elif gender == "ж" and bmi > 20 and bmi <= 26 and age > 40:
    print("Норма")
elif gender == "ж" and bmi > 26 and bmi <= 32 and age > 40:
    print("Высокий ИМТ.")
elif gender == "ж" and bmi > 32 and bmi <= 40 and age > 40:
    print("Ожирение 1-2 степени. Необходима консультация специалиста.")
elif gender == "ж" and bmi > 40 and bmi < 50 and age > 40:
    print("Ожирение 3 степени. Необходима срочная консультация специалиста.")
else:
    print("Введены не верные данные")
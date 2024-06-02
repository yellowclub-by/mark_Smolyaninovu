name = input("веддите своё имя ")
phone = input("веддите свой номер ")
grade = input("веддите свой класс ")
weight = float(input("веддите свой вес "))
allow = weight >= 40 and weight <= 60
print(f'''Привет ,{name.capitalize()}
номер - {phone}\nКласс{grade.strip("А Б В Г а б в г")}
Вес - {weight}
Порядковый номер {phone[-4 :]}
проверте допуск - {allow}

''')
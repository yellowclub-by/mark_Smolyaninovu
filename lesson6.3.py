# products = "хлеб, лук, мак, молоко, лимон, булочка"
# print(products.split())
# print(products.split(","))
# print(products.split(", "))


# name = "Саша"
# print(name)
# name = "Паша"
# print(name)


# products = "хлеб, лук, мак, молоко, лимон, булочка"
# print(products)
# products_lst = products.split(", ")
# print(products_lst)
# print(products)
# products = products.split(", ")
# print(products)


# info = "Марк, Смольянинов, 2013, +375296662170"
# info = info.split(", ")
# print(info)
# name = info[0]
# surname = info[1]
# age = info[2]
# tel = info[3]
# print(name)
# print(surname)
# print(age)
# print(tel)


info = input("ведите предмет, имя, балл через запятую и пробел: ")
info = info.split(", ")
print(info)
projects = info[0]
print(projects)
name = info[1]
print(name)
point = info[2]
print(point)

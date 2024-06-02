# grades = [8, 7, 5, 4, 7]
# grades.pop(-1)
# print(grades)
# grades.append(8)
# print(grades)


# grades = [8, 7, 5, 4, 7]
# final_grades = grades.pop(0)
# print(final_grades)
# print(grades)


# grades = [8, 7, 5, 4, 7]
# grades.insert(4, 6)
# print(grades)


# grades = [8, 7, 5, 4, 7]
# # grades.index(4)
# # print(grades.index(4))
# # ans = grades.index(4)
# # print(ans)
#
#
# grades = [8, 7, 5, 4, 7]
# # grades.index(7)
# ans = grades.index(7, 2)
# print(ans)


# grades = [8, 7, 5, 4, 7]
# grades.clear()
# print(grades)

grades = [8, 7, 5, 4, 7]
grades2 = grades[:]
grades.clear()
print(grades)
print(grades2)


produtcs = input("ведите продукты через запятую пробел")
produtcs = produtcs.split(", ")
print(produtcs)


print(produtcs[0])
print(produtcs[-1])
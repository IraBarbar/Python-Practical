# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# list1 = ['jgjgjgj','klkgslk85fsdk', 'fjsfj85sskss' ]
# print(list1)
# x = '11'
# for n in range(0,len(list1)):
#     if x in list1[n]:
#         print(n)
# else:
#     print('no')

# 3. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1

n1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
n2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
n3= ["йцу", "фыв", "ячс", "цук", "йцукен"]

x = 'qwe'
count = 0
for i in range(0,len(n1)):
    if x == n1[i]:
        count = count+1
    if count ==2:
        print(x,i)
        break
else:
    print(x,'-no')
 
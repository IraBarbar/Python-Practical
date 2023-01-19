# 3. Создайте словать заданный по формуле 3*n+1, где n это ключ, 
# а формула значение
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# my_dict = {}
# number = int(input('Введите целое число: '))

# for n in range(1,number +1):
#     my_dict[n] = 3*n+1

# print(my_dict)

# my_string = 'питон самый лучший язык в мире'
# my_string = my_string.split('и')
# print(my_string)

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью математических формул нахождения корней квадратного уравнения

my_string = '3*x**2 + 5*x -6 = 0'
import math

my_string_int = None
my_num = []

# x = b**2-4*a*c
my_string = my_string.replace('0', '').replace('=', '').replace(' ', '').replace('+', ' ').replace('-', ' -')
print(my_string)
my_string_int = my_string.split() 
print(my_string_int)
for i in my_string_int:
    if i.startswith('x'):
        my_num.append(1)
    elif i.startswith('-x'):
        my_num.append(-1)
    else:
        my_num.append(int(i.split('*')[0]))

print(my_num)

a = my_num[0]
b = my_num[1]
c = my_num[2]
disc = b**2 - 4*a*c
if disc > 0:
    x1 = (-b - math.sqrt(disc))/(2*a)
    x2 = (-b + math.sqrt(disc))/(2*a)
    print(x1, x2)
elif disc ==0:
    x = (-b - math.sqrt(disc))/(2*a)
    print(x)
else:
    None





        

                


# https://www.youtube.com/watch?v=U0U8Ddx4TgE&ab_channel=AlekOS

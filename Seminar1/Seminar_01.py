# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

#     *Примеры:*

#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# if a**2 == b or b**2 == a:
#     print(f'Yes {a} ')
# else:
#     print('No')

# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

my_list = []
for i in range(5):
    my_list.append(int(input(f'Введите число № {i+1}: ') ))

print(my_list)
list_max = my_list[0]
for i in range(1,len(my_list)):
    if list_max < my_list[i]:
        list_max = my_list[i]

print(list_max)

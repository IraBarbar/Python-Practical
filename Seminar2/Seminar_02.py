# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

#num = int(input('Введите целое число: '))

# for degree in range(num):
#     print((-3)**degree, end=' ')

# 1. Напишите программу, которая будет на вход принимать число 
# N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     при 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num = int(input('Введите целое число: '))
# if num < 0:
#     num = -num
# for i in range(-num, num+1, 1):
#         print(i, end=' ')
    



# 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# num = float(input('Введите целое число: '))
# res = num%1*10
# print(int(res))

# n = float(input('Enter number '))

# if (int(n) == n):
#     print('no')
# else:
#     print(int(abs(n) * 10) % 10)
#https://discord.com/channels/1043910574045667448/1046319022016299108/1046319558404882462

# num = float(input('Введите вещественное число: '))
# if num == int(num):
#     print('НЕТ!')
    
# else:
#     if num<0:
#         num = -num
#     res = int(num*10 % 10)
#     print(res)

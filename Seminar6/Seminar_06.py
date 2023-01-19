# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# *Пример:*

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# my_list  = []
# data = [1, 2, 3, 5, 1, 5, 3, 10]
# for i in range(len(data)) :
#     if data.count(data[i]) ==1:
#         my_list.append(data[i])
# print(my_list)

# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;

import math
string = '-11-5*2-(2-1)+21/3*(3+4)+(-15*3)'
print(string)

def replace_math_symbol(data):
    synbol = ['*', '/', '+', '-', '(', ')']
    for i in synbol:
        data = data.replace(i, ' ' + i + ' ')
    data = data.split()
    for i in range(len(data)):
        if data[i] == '-' and i == 0:
            data[i+1] = data[i]+data[i+1]
            data[i] = 'del'
        elif data[i] == '(' and data[i+1] == '-':
            data[i+2] = data[i+1]+data[i+2]
            data[i+1] = 'del'
        elif data[i] == '*' and data[i+1] == '-':
            data[i+2] = data[i+1]+data[i+2]
            data[i+1] = 'del'
        elif data[i] == '/' and data[i+1] == '-':
            data[i+2] = data[i+1]+data[i+2]
            data[i+1] = 'del'
    data = list(filter((lambda x: x != 'del'), data))
    return data
    
string = replace_math_symbol(string)

def task_plus(data):
    for j in range(len(data)):
        if data[j] == '+':
            data[j+1] = int(data[j-1]) + int(data[j+1])
            data [j] , data[j-1] = 'del', 'del'
    data = list(filter((lambda x: x != 'del'), data))
    return data
def task_minus(data):
    for j in range(len(data)):
        if data[j] == '-':
            data[j+1] = int(data[j-1]) - int(data[j+1])
            data [j] , data[j-1] = 'del', 'del'
    data = list(filter((lambda x: x != 'del'), data))
    return data
def task_generation(data):
    for j in range(len(data)):
        if data[j] == '*':
            data[j+1] = int(data[j-1]) * int(data[j+1])
            data [j] , data[j-1] = 'del', 'del'
    data = list(filter((lambda x: x != 'del'), data))
    return data
def task_degree(data):
    for j in range(len(data)):
        if data[j] == '/':
            data[j+1] = round(int(data[j-1]) / int(data[j+1]))
            data [j] , data[j-1] = 'del', 'del'
    data = list(filter((lambda x: x != 'del'), data))
    return data

def math_from_string_to_result(data):
    new_data =[]
    if '(' in data:
        count = data.count('(')
        start = []
        end =[]
        for i,item in enumerate(data) :
            if item == '(':
                start.append(i)
            elif item == ')':
                end.append(i)
        for i in range(count) :
            x=data[start[i]+1:end[i]]
            new_data.append(x)
            for j in range(start[i],end[i]+1):
                data[j] = 'del'     
    for i in range(len(new_data)) :
        new_data[i] = task_degree(new_data[i])
        new_data[i] = task_generation(new_data[i])
        new_data[i] = task_minus(new_data[i])  
        new_data[i] = task_plus(new_data[i])
    a = []    
    for i in new_data:
        for j in i:
            a.append(j)
    for j in range(count):
        for i in range(len(data)) :
            if i == start[j]:
                data[i] = a[j]
    data = list(filter((lambda x: x != 'del'), data))
    data = task_degree(data)
    data = task_generation(data)
    data = task_minus(data)  
    data = task_plus(data)
    result = f'result = {data[0]}'
    return result
print(math_from_string_to_result(string))
    
                  



            




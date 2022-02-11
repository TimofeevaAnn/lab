#!/usr/bin/env python
# coding: utf-8

# # Лабораторная работа №1
# ## Выполнил студент Тимофеева Анна БВТ2005
# 

# ### Оглавление
# 1. [Задание 1](#Задание-№1)
# 2. [Задание 2](#Задание-№2)
# 3. [Задание 3](#Задание-№3)
# 4. [Вывод](#Вывод)

# ### Задание №1
# <i> Вызвать функцию print() и передать туда строку Hello, World! </i>

# In[16]:


print('Hello, World!')


# ### Задание №2
# Написать генератор случайных матриц(многомерных), который принимает
# опциональные параметры <b>m</b>, <b>n</b>, <b>min_limit</b>, <b>max_limit</b>, где <b>m</b> и <b>n</b> указывают размер
# матрицы, а <b>min_lim</b> и <b>max_lim</b> - минимальное и максимальное значение для
# генерируемого числа.

# In[24]:


import random
import time


# In[25]:


user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())
user_m, user_n, user_min_limit, user_max_limit
matrix = [[random.randrange(user_min_limit,user_max_limit) for y in range(user_m)] for x in range(user_n)]

for im in range(user_n):
    print(matrix[im])


# ### Задание №3
# Реализовать методы сортировки строк числовой матрицы в соответствии с
# заданием. Оценить время работы каждого алгоритма сортировки и сравнить его со
# временем стандартной функции сортировки. Испытания проводить на сгенерированных
# матрицах.

# In[3]:


import copy
import time


# In[16]:


# Сортировка выбором.
# Берётся срез массива, в котором минимальный элемент переносят в самый левый угол,
# после чего срез уменьшается и цикл повторяется.

start_time = time.time()
arr = [3,2,5,4,8,2,221]
K = len(arr)

for i in range(0,K-1):
    m = arr[i]
    p = i
    for j in range(i+1, K):
        if m > arr[j]:
            m = arr[j]
            p = j
        if p != i:
            t = arr[i]
            arr[i] = arr[p]
            arr[p] =  t
print(arr)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# In[26]:


# Сортировка вставкой.
start_time = time.time()
def sort_select(line):
    for i in range (len(line)):
        a=line[i]
        for j in range (i+1,len(line)):
            if line[j]<line[i]:
                line[i]=line[j]
                line[j]=a
for line in matrix:
    line=sort_select(line)
print(matrix)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# In[30]:


# Сортировка обменом. || Сортировка пузырьком.
start_time = time.time()
def sort_trade(line):
    for i in range(0,len(line)-1):
        a = line[i]
        if line[i]>line[i+1]:
            line[i] = line[i+1]
            line[i+1] = a
    return line
for line in matrix:
    line=sort_trade(line)
print(matrix)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# In[7]:


# Сортировка Шелла.
start_time = time.time()
#TODO
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# In[8]:


# Быстрая сортировка.
start_time = time.time()
#TODO
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
    


# In[9]:


# Турнирная сортировка.
start_time = time.time()
#TODO
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# ### Вывод
# 

# In[ ]:


Я научилась делать почти все, что нужно было в лабораторной.


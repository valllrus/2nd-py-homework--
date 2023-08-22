#Задача №10

# import random
# from random import randint

# coin_quantity = int(input('введите количество монет: '))


# u = 0
# q = 0
# coins = [0, 1]
# for i  in range(coin_quantity):
#     random.shuffle(coins)
#     print(f'общее количество монет{coins}')
#     if int(coins[0]) == 0:
#         q += 1
#     if int(coins[0]) == 1:
#         u += 1
# print(f'всего монет {u, q}')

# if u > q:
#     ansver = q
# else:
#     ansver = u

# print(f'минимальное количество монет, которое нужно перевернуть: {ansver}')

# Задача №12

S = int(input('введите сумму чисел: '))
P = int(input('введите произведение чисел: '))

X = (S-int((S**2-4*P)**0.5))//2
Y = S - X
if X<=1000 and Y<=1000:
   print(f'числа, задуманные петей: {X, Y}')

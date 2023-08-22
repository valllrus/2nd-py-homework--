#Задача №10

import random
from random import randint

coin_quantity = int(input('введите количество монет: '))


u = 0
q = 0
coins = [0, 1]
for i  in range(coin_quantity):
    random.shuffle(coins)
    print(f'общее количество монет{coins}')
    if int(coins[0]) == 0:
        q += 1
    if int(coins[0]) == 1:
        u += 1
print(f'всего монет {u, q}')

if u > q:
    ansver = q
else:
    ansver = u

print(f'минимальное количество монет, которое нужно перевернуть: {ansver}')
#1
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)

#2
import random
random_numbers = [random.randint(0, 100) for _ in range(100)]
user_number = int(input("Введите число: "))
count = random_numbers.count(user_number)
print(f"Число {user_number} звстречается {count} раз.")

#3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements)

#4
import random
lottery_numbers = random.sample(range(1, 43), 5)
user_numbers = list(map(int, input("Введите 5 чисел через пробел: ").split()))

matches = len(set(lottery_numbers) & set(user_numbers))

if matches == 3:
 print("Вы выиграли 100 гривен!")
elif matches == 4:
 print("Вы выиграли 500 гривен!")
elif matches == 5:
 print("Вы выиграли 2500 гривен!")
else:
 print("К сожалению, вы не выиграли.")

#5
import random
M=3
N=4
matrix = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

positive = 0
negative = 0
zero = 0

for row in matrix:
    for num in row:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

print(f"Положительные: {positive}, Отрицательные: {negative}, Нулевые: {zero}")

#6
import random

M = 5
N=10
K = 3

seats = [[random.randint(0, 1) for _ in range(N)] for _ in range(M)]

def can_sell_tickets(seats, K):
 for row in seats:
     consecutive = 0
     for seat in row:
         if seat == 0:
             consecutive += 1
             if consecutive == K:
                 return True
         else:
             consecutive = 0
 return False

print("Начальный список мест:")
for row in seats:
 print(row)

if can_sell_tickets(seats, K):
 print(f"Можно продать билеты на соседние места {K}.")
else:
 print(f"Невозможно продать билеты на соседние места {K}.")
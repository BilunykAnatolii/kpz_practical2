a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

count = 0

if a % 1 == 0:
    count += 1
if b % 1 == 0:
    count += 1
if c % 1 == 0:
    count += 1

print("Кількість цілих чисел: ", count)

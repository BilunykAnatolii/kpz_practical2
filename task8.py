a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

count = 0

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print("Кількість додатних чисел: ", count)

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))

if a != b:
    max_number = max(a, b)
    a = max_number
    b = a
else:
    a = 0
    b = 0

print("Результат:")
print("a =", a)
print("b =", b)

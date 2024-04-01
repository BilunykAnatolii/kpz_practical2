x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x == y:
    print("Числа x та y не можуть бути однаковими.")
else:
    if x < y:
        x = (x + y) / 2
        y = 2 * x
    else:
        y = (x + y) / 2
        x = 2 * y

    print("Після обробки:")
    print("x =", x)
    print("y =", y)

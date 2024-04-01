a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
k = int(input("Введіть число k: "))

divisors = []

if a % k == 0:
    divisors.append("a")
if b % k == 0:
    divisors.append("b")
if c % k == 0:
    divisors.append("c")

if divisors:
    print(f"Число {k} є дільником чисел: {', '.join(divisors)}")
else:
    print(f"Число {k} не є дільником жодного з чисел")

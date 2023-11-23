a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
d = int(input("Введите значение d: "))
def calculate_composers(a, b, c, d):
    for _ in range(a, b):
        c = (c + d) ** 2
    return int(c)
result = calculate_composers(a, b, c, d)
print(f"{result}")
a = input("Введите слово: ")
b = ""
c = 0
for d in a:
    if c % 3 == 2:
        b = b + d
    c += 1
print(b)
score=input("Введите счет:").strip()
a,b = score.split(":")
a=int(a)
b=int(b)
if a>b:
    print(1)
elif a<b:
    print(2)
else:
    print(0)

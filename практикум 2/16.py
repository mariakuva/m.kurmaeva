a=int(input("Введите PIN-код:"))
if a>=1000 and a<=9999:
    if not (a>=1900 and a<=2050):
        d1=a//1000
        d2=(a//100)%10
        d3=(a//10)%10
        d4=a%10
        if (d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4):
            print("OK")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")
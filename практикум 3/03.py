while True:
    a = int(input("Введите число: "))
    i = 1
    while i * i < a:
        i += 1
    if i * i == a:
        print("Это полный квадрат.")
        break
    else:
        print("Это не полный квадрат. Попробуйте еще раз.")
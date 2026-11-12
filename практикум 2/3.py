print("Вы поедете на бал?")
a=input("Ответ:").strip().lower()
if not (a=="да" or a=="нет"):
    print("Верно")
else:
    print("Неверно")
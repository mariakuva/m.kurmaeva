N = int(input("Введите число N: "))
s = 1
questions = 0
while s < N:
    s = s * 2
    questions += 1
print(questions)
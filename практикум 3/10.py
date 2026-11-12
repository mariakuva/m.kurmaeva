p_temp = float(input())
count = 0
while True:
    n_temp = float(input())
    if n_temp == 0:
        break
    if n_temp < p_temp:
        count += 1
    p_temp = n_temp
print(count)
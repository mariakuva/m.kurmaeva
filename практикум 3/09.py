N, K, R = map(int, input().split())
d = N
day = 1
while d < R:
    d = d + (d * K / 100)
    day += 1
print(day)
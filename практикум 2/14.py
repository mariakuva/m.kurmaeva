n=int(input())
g=n//493
n=n%493
s=n//29
k=n%29
if g>0:
    print(g,"галлеон(ов)")
if s>0:
    print(s,"сикль(ей)")
if k>0:
    print(k,"кнат(ов)")

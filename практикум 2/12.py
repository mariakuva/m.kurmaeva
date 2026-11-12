p=int(input())
if p%10 == 1 and p!=11:
    print(p, "попугай")
elif (p % 10 == 2 or p % 10 == 3 or p % 10 == 4) and (p != 12 and p != 13 and p != 14):
    print(p, "попугая")
else:
    print(p, "попугаев")
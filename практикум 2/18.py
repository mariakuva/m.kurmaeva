o=input()
k=input()
a,b=map(int,o.split("x"))
c,d,e=map(int,k.split("x"))
mh=max(a,b)
nh=min(a,b)
mb=max(c,d,e)
nb=min(c,d,e)
sr=c+d+e-mb-nb
if nb<=nh and sr<=mh:
 print("да")
else:
 print("нет")
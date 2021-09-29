### FLAMES GAME
a=str(input("Enter your name1:-"))
b=str(input("Enter your name2:-"))
for i in a:
    for j in b:
        if i==j:
            a=a.replace(i,"",1)
            b=b.replace(j,"",1)
            break
c=len(a+b)
if c>0:
    l=["Friends","Lovers","Affectionate","Marrige","Enemies","Siblings"]
    while len(l)>1:
        r=c%len(l)
        i=r-1
        if i>=0:
            left=l[:i]
            right=l[i+1:]
            l=right+left
        else:
            l=l[:len(l)-1]
    print("Relationship is:-",l[0])
else:
    print("Enter a different name")

s ="CODER"
n=len(s)
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[i],end=" ")
    print()
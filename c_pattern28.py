s ="CODER"
n=len(s)
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(s[i],end=" ")
    for j in range(i):
        print(s[i], end=" ")
    print()
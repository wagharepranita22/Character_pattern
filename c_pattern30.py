s ="CODER"
n=len(s)
for i in range(n-1,-1,-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(s[i],end=" ")
    print()
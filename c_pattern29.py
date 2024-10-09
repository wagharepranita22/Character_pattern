s ="CODER"
n=len(s)
for i in range(n-1,-1,-1):
    for j in range(i,n):
        print(s[i],end=" ")
    print()
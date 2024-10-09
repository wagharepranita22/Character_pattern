s ="CODER"
n = len(s)
k = n-1
for i in range(n):
    p = k
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n):
        print(s[p],end=" ")
        p -= 1
    k -= 1
    print()
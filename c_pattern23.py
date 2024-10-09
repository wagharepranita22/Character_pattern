n = int(input("N : "))
for i in range(n):
    p = 69
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p -= 1
    print()
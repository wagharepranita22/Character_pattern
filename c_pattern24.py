n = int(input("N : "))
k =69
for i in range(n):
    p = k
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
        p += 1
    k -=1
    p =68
    for j in range(i):
        print(chr(p),end=" ")
        p -= 1
    print()
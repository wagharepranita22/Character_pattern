n = int(input(" n :"))
p = 69
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
    p -= 1
    print()
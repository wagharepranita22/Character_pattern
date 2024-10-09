n = int(input(" n : "))
p = 65
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1, n):
        print(chr(p),end=" ")
    for j in range(i, n):
        print(chr(p),end=" ")
    p += 1
    print()


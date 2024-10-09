n = int(input(" N : "))
for i in range(n):
    p = 65
    for j in range(i+1):
        print(chr(p), end=" ")
        p +=1
    for j in range(i+1,n):
        print(" ", end=" ")
    for j in range(i+1, n):
        print(" ", end=" ")
    p = 65
    for j in range(i+1):
        print(chr(p), end=" ")
        p += 1
    print()

for i in range(n):
    p = 65
    for j in range(i,n):
        print(chr(p), end=" ")
        p +=1
    for j in range(i):
        print(" ", end=" ")
    for j in range(i):
        print(" ", end=" ")
    p = 65
    for j in range(i, n):
        print(chr(p), end=" ")
        p += 1
    print()
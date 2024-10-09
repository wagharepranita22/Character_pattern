n = int(input(" n : "))
p = 65
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    for j in range(i):
        print(chr(p), end=" ")
    p +=1
    print()

for i in range(n+1):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i+1,n+1):
        print(chr(p), end=" ")
    for j in range(i,n+1):
        print(chr(p),end=" ")
    p -= 1
    print()
n = int(input(" n :"))
p = 70
for i in range(n):
    for j in range(i):
        print(chr(p),end=" ")
    p -= 1
    print()
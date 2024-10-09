n = int(input(" n :"))
p = 65
for i in range(n):
    for j in range(i+1):
        if i % 2 == 0:
            print("A",end=" ")
        else:
            print("B",end=" ")
    print()

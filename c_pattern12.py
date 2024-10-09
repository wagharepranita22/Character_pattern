n = int(input(" n :"))
p = 65
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        if i % 2 == 0:
            print("Z",end=" ")
        else:
            print("O",end=" ")
    print()

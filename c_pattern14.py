n = int(input("n : "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n):
        if i % 2 == 0:
            print("Z",end=" ")
        else:
            print("O",end=" ")
    for j in range(i,n):
        if i % 2 == 0:
            print("Z",end=" ")
        else:
            print("O",end=" ")
    print()

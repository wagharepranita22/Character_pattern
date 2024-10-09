n = int(input("n : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        if i % 2 == 0:
            print("A",end=" ")
        else:
            print("#",end=" ")
    for j in range(i):
        if i % 2 == 0:
            print("A",end=" ")
        else:
            print("#",end=" ")
    print()

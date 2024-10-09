n = int(input("Enter your n  value : "))
p = 65
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p), end=" ")
    p +=1
    print()
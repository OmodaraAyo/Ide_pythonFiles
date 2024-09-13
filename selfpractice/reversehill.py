def reverseHill(number):
    for i in range(1,number+1):
        for j in range(1,i):
            print(" ", end=" ")
        for k in range(1+number, i, -1):
            print("*", end=" ")
        for L in range(1+number, i, -1):
            print("*", end=" ")
        print()
    return ""
print(reverseHill(5))
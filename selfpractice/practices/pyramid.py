def pyramid(number):
    for i in range(1, number+1):
        for k in range(1+number, i, -1):
            print(" ", end=" ")
        for L in range(i, 0, -1):
            print(L, end=" ")
        for M in range(1, i):
            print(M+1, end=" ")
        print('')
    return ""

print(pyramid(5))
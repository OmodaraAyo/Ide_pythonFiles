def decrep(number):
    for i in range(1, number+1):
        for j in range(1+number, i, -1):
            print(" ", end=" ")
        for k in range(1, i+1, +1):
            print(k, end=" ")
        print()
    return ""

print(decrep(5))
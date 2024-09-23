def diamond(number):
    for i in range(1, number+1):
        for j in range(i, number+1):
            print(" ", end="  ")
        for k in range(1, i+1):
            print("*", end="  ")
        for L in range(1, i+1):
            print("*", end="  ")
        print()
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(" ", end="  ")
        for k in range(i, number+1):
            print("*", end="  ")
        for L in range(i, number+1):
            print("*", end="  ")
        print()
    return ""
print(diamond(5))
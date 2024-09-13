def nabla_del(number):
    for i in range(1, number+1):
        for j in range(number, i, -1):
            print(" ", end=" ")
        for k in range(1, i+1):
            print(" *", end=" ")
        for L in range(number, i, -1):
            print("  ", end=" ")
        for M in range(1, i+1):
            print(" *", end=" ")
        print()
    return ""
print(nabla_del(5))
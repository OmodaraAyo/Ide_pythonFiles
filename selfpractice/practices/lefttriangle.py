def left_triangle(number):
    for i in range(1, number+1):
        for k in range(1, i+1):
            print(" ", end=" ")
        for j in range(i, number+1):
            print("*", end=" ")
        print()
    return ""
print(left_triangle(5))
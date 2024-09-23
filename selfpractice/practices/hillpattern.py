def hillPattern(number):
    for i in range(1, number+1):
        for j in range(i, number):
            print("  ", end="")
        for k in range(1, i+1):
            print("* ", end="")
        for m in range(2, i+1):
            print("* ", end="")
        print()
    return ""
print(hillPattern(5))
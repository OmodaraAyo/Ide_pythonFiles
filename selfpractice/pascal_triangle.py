def ones_of_pyramid(number):
    for i in range(1, number+1):
        for j in range(1+number, i, -1):
            print(" ", end=" ")
        for k in range(1, i, +1):
            print(k, end=" ")
        for L in range(i, 0, -1):
            print(L, end=" ")
        print()
    return ""

while True:
    try:
        user_number = int(input("Enter a number: "))
        ones_of_pyramid(user_number)
        break
    except ValueError:
        print("Invalid input!!! Please enter a number")
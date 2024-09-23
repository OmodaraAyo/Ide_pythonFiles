def diamond_numbers_of(number):
    for i in range(1, number):
        for j in range(1+number, i, -1):
            print(" ", end=" ")
        for k in range(0,i):
            print(i, end=" ")
        for L in range(1,i):
            print(i, end=" ")
        print()
    for i, j in zip(range(number, 1, -1), range(1, number+1)):
        for k in range(0,j):
            print(" ", end="  ")
        for L in range(j, number):
            print(j+4, end=" ")
        print()
    return ""

while True:
    try:
        user_input = int(input("Enter a number: "))
        diamond_numbers_of(user_input)
        break
    except ValueError:
        print("Please enter a number")
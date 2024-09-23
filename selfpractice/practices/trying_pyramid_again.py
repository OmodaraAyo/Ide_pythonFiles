def my_pyramid(number):
    for i in range(1, number+1):
        for j in range(1+number, i, -1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        for L in range(1, i):
            print(L+1, end=" ")
        print()
    return ""

while True:
    try:
        user_input = int(input("Enter numbers between 1-13: "))
        if 1 <= user_input <= 13:
            my_pyramid(user_input)
            break
    except ValueError:
        print("Inavlid input!!! please enter a number between 1-13")
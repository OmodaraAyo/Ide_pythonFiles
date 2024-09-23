def set_triangle_of(numbers):
    for i in range(1, numbers+1):
        for j in range(1, i):
            print(" ", end=" ")
        for k in range(1, numbers+2-i, +1):
            print(k, end=" ")
        print()
    return ""

while True:
    try:
        user_input = int(input("Enter a number: "))
        set_triangle_of(user_input)
        break
    except ValueError:
        print("Please enter a number")
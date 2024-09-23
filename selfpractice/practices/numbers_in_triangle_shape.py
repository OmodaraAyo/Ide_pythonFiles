def top_to_bottom(number):
    for i in range(1, number+1):
        for j in range(1, number+2-i, +1):
            print(j, end=' ')
        print()
    return ""

while True:
    try:
        user_input =int(input("Enter a number: "))
        print(top_to_bottom(user_input))
        break
    except ValueError:
            print("Invalid input, try again.")

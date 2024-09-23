def biggest_odd(numbers):
    my_Number = []
    biggest_Odd_Number = 0
    for num in numbers:
        my_Number.append(int (num))
    for numbs in my_Number:
        if numbs % 2 != 0 and numbs > biggest_Odd_Number:
            biggest_Odd_Number = numbs
            numbs = biggest_Odd_Number
    return biggest_Odd_Number
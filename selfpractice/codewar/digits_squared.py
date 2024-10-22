def square_digits(number):
    newNumber = str(number)
    num = ""
    for i in range(len(newNumber)):
        my_num = int(newNumber[i])**2
        num += str(my_num)
    return int(num)
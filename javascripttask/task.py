def square_Sum_Of(first_Number, second_Number):
    return (first_Number + second_Number) ** 2

def scaled_Sum(number):
    return (number % 10) + number

def exponent_Of(number, exponent):
    return (number) ** exponent

def dividend_Of(number):
    x = number + 10
    y = number - 10
    z = number % 10
    return number / (x * y * z)

print(square_Sum_Of(5,5))
print()
print(scaled_Sum(7))
print()
print(dividend_Of(5))
print()
print(exponent_Of(10,2))
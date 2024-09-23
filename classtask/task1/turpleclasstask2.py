def zeros(numbers):
    array = []
    for i in range(4):
        array.append([numbers] * 4)
    return array


print(zeros(0))


score = 1,3,4, "bimbola"
single_tuple = 1, 2, 3,
great = list(score)
great[3] = 'Ayo'
great = tuple(great)
print(great)
print(single_tuple)

new_score = 1,2,4, [0,7,6], "AYO", "Dele"
new_score[3].extend([55,99])
print(new_score)
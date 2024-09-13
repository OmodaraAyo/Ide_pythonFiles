def swapchars(firstinput,secondinput):
    first_array = []
    second_array = []
    third_array = []
    output = ''
    output2 = ''
    for i, j in zip(range(len(firstinput)), range(len(secondinput))):
        first_array.append(firstinput[i])
        second_array.append(secondinput[j])
        third_array.append(secondinput[j])
    for i, j in zip(range(0, 2), range(0,2)):
        second_array[j] = first_array[i]
        first_array[i] = third_array[j]
    for i, j in zip(first_array, second_array):
        output += i
        output2 += j
    return output + ' ' +output2

def swapchars2(first_input,second_input):
    return second_input[:2] + first_input[2:]+ " " + first_input[:2] + second_input[2:]

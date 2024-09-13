def sees(first_input, second_input = "ce"):
    output = first_input[:3] + second_input + first_input[3:]
    return output

def cees(first_input, second_input = ['c','e']):
    output = []
    actual = ""
    for i in first_input:
        output.append(i)
    new_output = output[:3] + second_input + output[3:]
    for i in new_output:
        actual+= i
    return actual
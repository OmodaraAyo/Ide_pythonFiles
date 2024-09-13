def countCharss(user_input):
    my_dict = {}
    for char in user_input:
        my_dict[char] = (user_input.count(char))
    return my_dict

print(countCharss("semicolon.africa"))
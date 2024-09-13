def caps_to_small(user_input):
    upper_case = ""
    small_case = ""
    for char in user_input:
        if char.isupper():
            upper_case += char
        else:
            small_case += char
    return upper_case + small_case
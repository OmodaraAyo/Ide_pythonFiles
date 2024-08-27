def equal_strings(user_Input1, user_Input2):
    if len(user_Input1) == len(user_Input2):
        for i in range(len(user_Input1)):
            if str(user_Input1[i]) in user_Input2: return True
            else: return False
    else:
        return False
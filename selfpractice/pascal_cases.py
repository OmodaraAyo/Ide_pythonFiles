import re

def passPascalOf(user_input):
    new_input = re.split(r'[-_]', user_input)
    for i in range(len(new_input)):
        if i > 0:
            new_input[i] = new_input[i].capitalize()
    output = ''.join(new_input)
    return output

user_input = input('Enter any word: ')
print(passPascalOf(user_input))

# function _passPascalOf_Comments
# new_input = user_input.split('_')
# map(str, 'new_input')-> takes two parameters could be a function or an input
# output = ''.join(map(str, new_input))
#re.split -> returns the value as a turple
#"-,_,+,!".join are called seperators
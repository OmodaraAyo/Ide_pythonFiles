import string
from random import choices

def generate_password(length):
    try:
        int(length)
        if  8<=length<=16:
            patterns = (string.ascii_uppercase + string.ascii_lowercase + string.digits +
                string.punctuation.replace(string.punctuation, '@!$#'))
            program_choice = choices(patterns, k=length)
            password = ''.join(program_choice)
            return password
        else:
            return "password length must be between 8 and 16 characters"
    except ValueError:
        return "A length of password must be an integer"
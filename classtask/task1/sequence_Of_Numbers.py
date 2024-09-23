
def list_of(number,*args):
    numb = number + ','.join(args)
    new_number = numb.split(",")
    num2 = tuple(new_number)
    return f'{new_number},{num2}'
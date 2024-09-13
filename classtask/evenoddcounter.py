def eaocounter(my_list):
    even = 0
    odd = 0
    for i in my_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

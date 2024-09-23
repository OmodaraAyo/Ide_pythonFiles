def multiple_even(word, step):
    new_number = ""
    my_list = []
    if len(word) % 2 != 0:
       new_number = word + ("_" * (step - 1))
    else:
        new_number = word
    for i in range(0, len(new_number), step):
        my_list.append(new_number[i:i+step])
    return my_list

print(multiple_even("Ayodele", 2))

def split_sentence(word):
    my_array = word.split(' ')
    for i in range(len(my_array)):
        if len(my_array[i]) > 4:
            reverse_word = reverse_sentence(my_array[i])
            my_array[i] = reverse_word
    new_word = ' '.join(my_array)
    print(new_word)
    return new_word

def reverse_sentence(word):
    new_word = ""
    for i in range(len(word), 0, -1):
        new_word += word[i-1]
        print(new_word)
    return new_word

#using inbuilt function
# def split_sentence(word):
#     my_array = word.split(' ')
#     for i in range(len(my_array)):
#         if len(my_array[i]) > 4:
#             reverse_word = my_array[i][::-1]
#             my_array[i] = reverse_word
#     new_word = ' '.join(my_array)
#     print(new_word)
#     return new_word



# for j in range(len(my_array[i]) - 1, -1, -1):
#     end = (len(my_array[i]) - 1) - j
#     my_array[i] = my_array[i].replace(my_array[i][num], my_array[i][end])
#     num += 1

# my_array = word.split(" ")
#     for i in range(len(my_array)):
#            if len(my_array[i]) > 4:
#                num = 0
#                for j in range(len(my_array[i])):
#                    my_array[i] = my_array[i].replace(my_array[i][num],my_array[i][3])
#                    print(my_array[i])
#                    num += 1
#     new_word = " ".join(my_array)


def last_index(first_word, second_word):
    first_word_last_char = last_character(first_word)
    second_word_last_char = last_character(second_word)
    if first_word_last_char == second_word_last_char:
        return True
    else:
        return False

def last_character(word):
    last_alpha = ""
    for i in range(len(word), 0, -1):
        last_char = len(word) - 1
        if i == last_char:
            last_alpha = word[i]

    return last_alpha

def match_last_character(word, word2):
    new_word = word[-(len(word)):]
    if new_word == word2:
        return True
    else:
        return False


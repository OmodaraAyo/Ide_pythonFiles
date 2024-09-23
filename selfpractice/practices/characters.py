def dict_characters(word: str):
    my_dict = {}
    for character in word:
            my_dict [character.upper()] = my_dict.get(character.upper(), 0) +1
    return my_dict
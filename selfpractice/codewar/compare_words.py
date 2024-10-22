def solution(text, ending):
    length = if_statement(text, ending)
    newWord = ""
    for i in range(length, len(text)):
        newWord += text[i]

    if newWord == ending:
        return True
    else:
        return False


def if_statement(firstWord, secondWord):
    if len(firstWord) > len(secondWord):
        return len(firstWord) - len(secondWord)
    else:
        return len(secondWord) - len (firstWord)
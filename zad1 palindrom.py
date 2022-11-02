def check_is_palindrom(text):
    """
        Co literkę sprawdzaj każdą możliœa długość od najdłuższej
    """
    word_length = len(text)
    for i in range(word_length):
        if text[i] != text[-i-1]:
            return False
    return True


def check_whole_word(text):
    word_length = len(text)
    for i in range(word_length):
        is_palindrom = check_is_palindrom(text[i:word_length])
        if is_palindrom:
            return i
    return None


result = check_whole_word("teeteet")
if result is not None:
    print("Palindrom zaczyna się od znaku nr:", result+1, "(licząc indeks od zera to od numeru)", result)
else:
    print("Palindrom nie występuje")


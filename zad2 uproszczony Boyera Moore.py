def get_bad_char_heuristic(text, size):
    bad_char = [-1] * 256

    for i in range(size):
        bad_char[ord(text[i])] = i

    return bad_char


def search(source_text, pattern):
    pattern_length = len(pattern)
    text_length = len(source_text)
    bad_char = get_bad_char_heuristic(pattern, pattern_length)
    shift = 0
    while shift <= text_length-pattern_length:
        j = pattern_length-1
        while j >= 0 and pattern[j] == source_text[shift+j]:
            j -= 1
        if j < 0:
            return shift
        else:
            shift += max(1, j-bad_char[ord(source_text[shift+j])])
    return None
 

def main():
    print("Podaj tekst:")
    user_text = input()
    print("Podaj wyszukiwany patern:")
    user_password = input()

    search_res = search(user_text, user_password)
    if search_res is not None:
        print("Wyszukiwany patern zaczyna się od znaku nr:", search_res+1, " (indeks znaku licząc od 0 to:", search_res, ")")
    else:
        print("Nie znaleziono")

 
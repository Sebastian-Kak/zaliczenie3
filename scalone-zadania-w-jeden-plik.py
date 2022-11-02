def ex1():
    def check_is_palindrom(text):
        """
            Co literkę sprawdzaj każdą możliœa długość od najdłuższej
        """
        word_length = len(text)
        for i in range(word_length):
            if text[i] != text[-i - 1]:
                return False
        return True

    def check_whole_word(text):
        word_length = len(text)
        for i in range(word_length):
            is_palindrom = check_is_palindrom(text[i:word_length])
            if is_palindrom:
                return i
        return None

    print("Podaj słowo")
    user_word = input()
    result = check_whole_word(user_word)
    if result is not None:
        print("Palindrom zaczyna się od znaku nr:", result + 1, "(licząc indeks od zera to od numeru)", result)
    else:
        print("Palindrom nie występuje")


def dec2any():
    def convert_dec_to_any_with_value_list(number_in_dec, number_system):
        if number_in_dec == 0:
            return [0]
        digits = []
        while number_in_dec:
            new_char = int(number_in_dec % number_system)
            digits.append(new_char)
            number_in_dec //= number_system
        return digits[::-1]

    def value_list_to_string(value_list):
        big_a_in_ascii = 65
        output_string = ""
        for value in value_list:
            if value > 9:
                value -= 10
                value += big_a_in_ascii
                output_string += chr(value)
            else:
                output_string += str(value)
        return output_string

    def convert_dec_to_any(number_in_dec, number_system):
        result_as_value_list = convert_dec_to_any_with_value_list(number_in_dec, number_system)
        result_as_string = value_list_to_string(result_as_value_list)
        return result_as_string

    print("Wpisz liczbę całkowitą:")
    user_number_in_dec = int(input())
    print("Wpisz system liczbowy jako liczbę całkowitą (np.: 8, 16, 17):")
    user_number_system = int(input())

    print(convert_dec_to_any(user_number_in_dec, user_number_system))


def any2dec():
    def value_list_to_string(number_as_string, number_system):
        hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                            'B': 11,
                            'C': 12, 'D': 13, 'E': 14, 'F': 15}
        number_as_string = number_as_string.strip().upper()
        dec = 0
        length = len(number_as_string) - 1
        for digit in number_as_string:
            dec += hex_to_dec_table[digit] * number_system ** length
            length -= 1
        return dec

    print("Wpisz liczbę całkowitą w dowolnym systemie liczbowym:")
    user_number = input()
    print("Wpisz system liczbowy jako liczbę całkowitą (np.: 8, 16, 17):")
    user_number_system = int(input())

    print(value_list_to_string(user_number, user_number_system))


def algorythm_bm():
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
        while shift <= text_length - pattern_length:
            j = pattern_length - 1
            while j >= 0 and pattern[j] == source_text[shift + j]:
                j -= 1
            if j < 0:
                return shift
            else:
                shift += max(1, j - bad_char[ord(source_text[shift + j])])
        return None

    print("Podaj tekst:")
    user_text = input()
    print("Podaj wyszukiwany patern:")
    user_password = input()

    search_res = search(user_text, user_password)
    if search_res is not None:
        print("Wyszukiwany patern zaczyna się od znaku nr:", search_res + 1, " (indeks znaku licząc od 0 to:",
              search_res, ")")
    else:
        print("Nie znaleziono")


def main():
    print("\nZadanie 1 - palindrom")
    ex1()

    print("\nZadanie 2 - algorytm Boyera Moore'a")
    algorythm_bm()

    print("\nZadanie 3 - dec2any")
    dec2any()

    print("\nZadanie 4 - any2dec")
    any2dec()


if __name__ == "__main__":
    main()

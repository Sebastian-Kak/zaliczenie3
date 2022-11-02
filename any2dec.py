def value_list_to_string(number_as_string, number_system):
    hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
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

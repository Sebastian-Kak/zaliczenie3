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

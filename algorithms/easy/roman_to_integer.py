""" Easy """


def numeral_value(letter):
    if letter == 'I':
        return 1
    if letter == 'V':
        return 5
    if letter == 'X':
        return 10
    if letter == 'L':
        return 50
    if letter == 'C':
        return 100
    if letter == 'D':
        return 500
    if letter == 'M':
        return 1000


def roman_to_integer(roman: str) -> int:
    number = 0
    i = 0
    while i < len(roman):
        symbol_value = numeral_value(roman[i])
        if i + 1 < len(roman):
            second_symbol_value = numeral_value(roman[i + 1])
            if symbol_value >= second_symbol_value:
                number += symbol_value
                i += 1
            else:
                number += second_symbol_value - symbol_value
                i += 2
        else:
            number += symbol_value
            i += 1
    return number


if __name__ == "__main__":

    while True:
        print("Please enter a roman numeral to convert: ")
        ip = input()
        if ip == "exit":
            break
        else:
            print("The number is: ", roman_to_integer(ip))


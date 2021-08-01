""" Medium Difficulty"""


def integer_to_numeral(num: int) -> str:
    if num == 1:
        return 'I'
    if num == 5:
        return 'V'
    if num == 10:
        return 'X'
    if num == 50:
        return 'L'
    if num == 100:
        return 'C'
    if num == 500:
        return 'D'
    if num == 1000:
        return 'M'


def numeral_calculation_loop(num, num_key, numeral):
    div = count = num // num_key
    while count:
        numeral += integer_to_numeral(num_key)
        count -= 1
    num -= (num_key * div)
    return num, numeral


def integer_convert_roman(num: int) -> str:
    numeral = ""
    if (num // 1000) >= 1:
        num, numeral = numeral_calculation_loop(num, 1000, numeral)
    if (num // 900) >= 1:
        numeral += "CM"
        num -= 900
    if (num // 500) >= 1:
        num, numeral = numeral_calculation_loop(num, 500, numeral)
    if (num // 400) >= 1:
        numeral += "CD"
        num -= 400
    if (num // 100) >= 1:
        num, numeral = numeral_calculation_loop(num, 100, numeral)
    if (num // 90) >= 1:
        numeral += "XC"
        num -= 90
    if (num // 50) >= 1:
        num, numeral = numeral_calculation_loop(num, 50, numeral)
    if (num // 40) >= 1:
        numeral += "XL"
        num -= 40
    if (num // 10) >= 1:
        num, numeral = numeral_calculation_loop(num, 10, numeral)
    if (num // 9) >= 1:
        numeral += "IX"
        num -= 9
    if (num // 5) >= 1:
        num, numeral = numeral_calculation_loop(num, 5, numeral)
    if (num // 4) >= 1:
        numeral += "IV"
        num -= 4
    if (num // 1) >= 1:
        num, numeral = numeral_calculation_loop(num, 1, numeral)
    return numeral


if __name__ == '__main__':

    while True:
        print("Please enter a number to convert to numerals: ")
        user_in = int(input())
        if user_in == 0:
            break
        print(integer_convert_roman(user_in))

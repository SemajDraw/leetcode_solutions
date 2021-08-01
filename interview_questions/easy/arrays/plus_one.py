
def plusOne(digits: list):
    if len(digits) == 1:
        if digits[0] == 9:
            digits[0] = 1
            digits.append(0)
        else:
            digits[0] += 1
        return digits
    if digits[-1] == 9:
        i = 1

        while digits[-1] == 9 or digits:
            digits.pop()
            i += 1
        j = 1
        while j < i:
            if j == 1:
                digits.append(1)
            digits.append(0)
            j += 1
    else:
        digits[-1] = digits[-1] + 1
    return digits


if __name__ == '__main__':
    digits = [9]
    print(plusOne(digits))
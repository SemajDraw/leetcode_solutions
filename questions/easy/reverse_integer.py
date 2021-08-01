""" Easy """

def reverse(x: int) -> int:
    str_num = str(x)
    minus = False
    if str_num[0] == '-':
        minus = True
        str_num = str_num[1:]
    rev_num = str_num[::-1]
    if minus:
        rev_num = '-' + rev_num
    rev_num = int(rev_num)
    return rev_num if abs(rev_num) < (1 << 31) - 1 else 0


if __name__ == "__main__":

    print(reverse(-345))


def palindrome_number(x: int) -> bool:
    str_num = str(x)
    if str_num[0] == '-':
        return False
    elif str_num == str_num[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome_number(-101))
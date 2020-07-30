"""Medium Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""


def invoke_generate_parentheses(num: int) -> list:
    parentheses_list = [""] * (2 * num)
    valid_parentheses = []
    generate_parentheses(parentheses_list, valid_parentheses, num, 0, 0, 0)
    return valid_parentheses


def generate_parentheses(parentheses_list, valid_parentheses, num, pos, open, close) -> list:

    if close == num:
        parentheses = ""
        for i in parentheses_list:
            parentheses += i
        return valid_parentheses.append(parentheses)
    if open > close:
        parentheses_list[pos] = ")"
        generate_parentheses(parentheses_list, valid_parentheses, num, pos + 1, open, close + 1)
    if open < num:
        parentheses_list[pos] = "("
        generate_parentheses(parentheses_list, valid_parentheses, num, pos + 1, open + 1, close)


if __name__ == '__main__':
    print(invoke_generate_parentheses(2))

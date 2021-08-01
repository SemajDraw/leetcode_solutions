"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""


def checkParentheses(parenthesesString: str):
    Rmin = Rmax = 0
    for c in parenthesesString:
        if c == '(':
            Rmax += 1
            Rmin += 1
        if c == ')':
            Rmax -= 1
            Rmin = max(Rmin - 1, 0)
        if c == '*':
            Rmax += 1
            Rmin = max(Rmin - 1, 0)
        if Rmax < 0:
            return False
    return Rmin == 0


if __name__ == '__main__':

    parenthesesString = '(*)'
    print(checkParentheses(parenthesesString))

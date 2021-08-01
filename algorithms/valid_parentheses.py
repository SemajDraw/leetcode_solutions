
def valid_parentheses(parentheses: str) -> bool:
    open = ('(','{','[')
    closed = (')','}',']')
    paren_stack = []
    for character in parentheses:
        if character in open:
            paren_stack.append(character)
        elif character in closed:
            indx = closed.index(character)
            if (len(paren_stack) > 0) and (open[indx] == paren_stack[-1]):
                paren_stack.pop()
            else:
                return False

    if len(paren_stack) == 0:
        return True


if __name__ == "__main__":

    parentheses = "()[]{}"
    parentheses1 = ""
    print(valid_parentheses(parentheses1))
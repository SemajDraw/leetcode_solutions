
def prefixFinder(array, prefix):
    validPrefixs = []
    for word in array:
        if word[:len(prefix)] == prefix:
            validPrefixs.append(word)

    return validPrefixs


if __name__ == '__main__':
    array = ['dog','dark','cat','door', 'dodge']
    prefix = 'do'
    print(prefixFinder(array, prefix))
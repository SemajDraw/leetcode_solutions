

def longest_common_prefix(words: list) -> str:
    prefix = ""
    index = 0
    word_count = 0
    if len(words) == 0:
        return prefix
    for letter in words[0]:
        for word in words:
            try:
                if letter == word[index]:
                    word_count += 1
            except IndexError:
                return prefix
        if word_count == len(words):
            prefix += letter
        else:
            break
        index += 1
        word_count = 0
    return prefix


if __name__ == "__main__":

    string_list = [
        "flower", "flow", "flight"
    ]
    string_list2 = [
        "aa", "a"
    ]
    print(longest_common_prefix(string_list2))
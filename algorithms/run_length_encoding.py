# aaaabbccccaaahhh
# Run length encode the input (4a2b3c1a)

def run_length_encode(s: str) -> str:
    encoded = ''
    if not s: return encoded
    if len(s) <= 1: return s
    count = 0
    prev = ''

    for i in range(0, len(s)):
        if s[i] == prev:
            count += 1
        elif prev != '':
            encoded += str(count) + prev
            prev = s[i]
            count = 1
        else:
            prev = s[i]
            count = 1
        
    encoded += str(count) + prev

    print(encoded)
     

if __name__ == '__main__':

    s = 'aaaabbcccaaahggg'
    run_length_encode(s)

    s1 = 'abcd'
    run_length_encode(s1)

    s2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    run_length_encode(s ,2)
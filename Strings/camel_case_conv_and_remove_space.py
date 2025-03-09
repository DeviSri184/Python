# http://geeksforgeeks.org/problems/convert-sentence-to-camel-case/1?selectedLang=python3


def convert_camel(s):
    s = list(s)
    cap = False
    write = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cap = True
        else:
            if cap and 'a' <= s[i] <= 'z':
                s[write] = chr(ord(s[i]) - 32)
            else:
                s[write] = s[i]
            cap = False
            write += 1
    return "".join(s[:write])

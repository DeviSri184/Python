# https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1?selectedLang=python3

def panagram(s):
    val = set(
    for i in s:
        if 'a' <= i <= 'z':
            s.add(i)
        elif 'A' <= i <='Z':
            s.add(chr(ord(i) + 32))

    return len(s) == 26

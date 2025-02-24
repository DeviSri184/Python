def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

print(are_anagrams("Astronomer", "Moon starer"))


"""Another Approach"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hash_map = defaultdict(int)

    for i in s:
        hash_map[i] += 1
    for i in t:
        if hash_map[i] == 0:
            return False
        hash_map[i] -= 1
    return True


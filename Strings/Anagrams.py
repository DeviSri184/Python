def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

print(are_anagrams("Astronomer", "Moon starer"))


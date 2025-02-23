val = "Hello World!"
vowels = "aeiouAEIOU"
vowel_count = cons_count = 0


for i in val:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            cons_count += 1

print("Vowels: {} Consonants: {}".format(vowel_count, cons_count))

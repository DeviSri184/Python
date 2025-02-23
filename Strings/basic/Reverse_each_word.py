orig_str = "Python is good programming language"

"""Using Inbuilt functions"""

print(" ".join(word[::-1] for word in orig_str.split()))

"""Using loop"""

start = 0
end = None
next_start = None

for i in range(len(name)):
    if i == len(name) - 1:
        end = i
    elif name[i] == ' ':
        end = i-1
        next_start = i+1
    if end:
        size = (end - start) + 1
        length = size // 2
        for j in range(length):
            name[start+j], name[end-j] = name[end-j], name[start+j]

        start = next_start
        end = None
print(orig_str)
print("".join(name))

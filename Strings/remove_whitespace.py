orig_str = "All the Best"

val = list(orig_str)


"""Using loop"""
for i in range(len(val)):
    if val[i] == ' ':
        val[i] = ''
print("".join(val))


"""Using replace function"""
print(orig_str.replace(" ", ""))

print("".join(orig_str.split()))

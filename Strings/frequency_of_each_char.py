orig_str = "Learn Python Programming"
hash_map = {}
for i in range(len(orig_str)):
    if orig_str[i] not in hash_map:
        hash_map[orig_str[i]] = 1
    else:
        hash_map[orig_str[i]] += 1

print("\n".join(f"{k}: {v}" for k, v in hash_map.items()))


"""Same above approach with diff syntax"""
for i in orig_str:
    hash_map[i] = hash_map.get(i, 0) + 1

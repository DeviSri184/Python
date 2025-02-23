val = "Learn"

"""Even indexed"""
print("\n".join(val[1::2]))


"""Odd Indexed"""
print("\n".join(val[::2]))


print("\n".join([val[i] for i in range(1, len(val), 2)]))     # Even Indexed

print("\n".join([val[i] for i in range(0, len(val), 2)]))     # Odd Indexed

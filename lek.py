chars = {}
for c in text:
    lowered = c.lower()
    if lowered in chars:
        chars[lowered] += 1
    else:
        chars[lowered] = 1
print(chars)

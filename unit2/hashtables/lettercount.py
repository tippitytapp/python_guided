
def letter_count(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts



print(letter_count('abaacabdbabcbabcba'))
import string

str = input()
letter = digit = other = 0
for s in str:
    if s in string.ascii_letters:
        letter = letter + 1
    elif s in string.digits:
        digit = digit + 1
    else:
        other = other + 1
print("letter = {},digit = {},other = {}".format(letter, digit, other))

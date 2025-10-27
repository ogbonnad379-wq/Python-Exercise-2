def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


for ch in ['a', 'H', 'A', '3', 'g']:
    if islower(ch):
        print(f"{ch} is lower")
    else:
        print(f"{ch} is upper")

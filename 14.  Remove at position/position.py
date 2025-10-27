def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str


print(remove_char_at("Best School", 0))
print(remove_char_at("Chicago", 2))
print(remove_char_at("is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

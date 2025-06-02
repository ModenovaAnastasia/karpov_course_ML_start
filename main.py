def check_string(string):
    if string != string.strip():
        return False
    string = string.strip()
    if not string.endswith('.'):
        return False
    words = string[:-1].split()
    if not words:
        return False
    first = words[0]
    if not (
        (len(first) == 1 and first.isupper()) or
        (len(first) > 1 and first[0].isupper() and first[1:].islower())
    ):
        return False
    for word in words[1:]:
        if not word.islower():
            return False
    return True

print(check_string('В этом году будет особенно теплое море.'))
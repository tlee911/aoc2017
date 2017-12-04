

def validate_passphrase(passphrase):
    words = passphrase.rstrip().split()
    counts = [words.count(word) for word in words]
    return max(counts) <= 1

assert validate_passphrase('aa bb cc dd ee') == True
assert validate_passphrase('aa bb cc dd aa') == False
assert validate_passphrase('aa bb cc dd aaa') == True

with open('input.txt') as file:
    input = file.readlines()
valid = [validate_passphrase(phrase) for phrase in input].count(True)
print(valid)
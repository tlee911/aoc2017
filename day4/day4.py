import itertools
import sys

INPUT_PATH = 'input.txt'

def get_words(password):
    return password.rstrip().split()

def check_duplicates(password):
    words = get_words(password)
    counts = [words.count(word) for word in words]
    return max(counts) <= 1

def check_anagrams(password):
    if not check_duplicates(password):
        # duplicate word is an anagram
        return False
    else:
        words = get_words(password)
        for word in words:
            anagrams = [''.join(p) for p in itertools.permutations(word)]
            for a in anagrams:
                if a in words and a != word:
                    # don't count the current word!
                    return False
    return True

def check_passwords(input, check_function):
    return [check_function(password) for password in input].count(True)


assert check_duplicates('aa bb cc dd ee') == True
assert check_duplicates('aa bb cc dd aa') == False
assert check_duplicates('aa bb cc dd aaa') == True

assert check_anagrams('abcde fghij') == True
assert check_anagrams('abcde xyz ecdab') == False
assert check_anagrams('a ab abc abd abf abj') == True
assert check_anagrams('iiii oiii ooii oooi oooo') == True
assert check_anagrams('oiii ioii iioi iiio') == False


with open(INPUT_PATH) as file:
    input = file.readlines()

no_dupes = check_passwords(input, check_duplicates)
no_anagrams = check_passwords(input, check_anagrams)

print('Passwords in input: {lines}'.format(lines=len(input)))
print('Without duplicate words: {no_dupes}'.format(no_dupes=no_dupes))
print('Without anagrams: {no_anagrams}'.format(no_anagrams=no_anagrams))



# %% [markdown]
# Given a string, calculate the number of consonants present using recursion.

# %% [markdown]
# Data.
# %% [codecell]
strings = ["GeorgeBitsonis", "TheofanisBitsonis", "SophiaBitsoni"]
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# %% [markdown]
# Iterative count.
# %% [codecell]
def iterative_character_count(string_):
    vowel = 0
    consonant = 0
    symbol = 0
    for letter in string_:
        if letter.lower() in vowels:
            vowel +=1
        elif letter.lower() in consonants:
            consonant += 1
        else:
            symbol += 1
    return {"vowels": vowel, "consonants": consonant, "symbols": symbol}

# %% [markdown]
# Recursive count.
# %% [codecell]
def recursive_symbol_count(string_):
    # vowel = 0
    # consonant = 0
    # symbol = 0
    if string_ == "":
        return 0 
    if string_.lower() not in vowels and string_[0].isalpha():
        return 1 + recursive_symbol_count(string_[1:])
    else:
        return recursive_symbol_count(string_[1:])
# %% [codecell]
for string in strings:
    print(iterative_character_count(string))
    print(iterative_character_count(string)['symbols'])
    print(recursive_symbol_count(string))
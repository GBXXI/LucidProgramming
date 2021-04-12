
# %% [markdown]
# Problem:<br>
#  Two strings. Check if they are anagrams.

# %% [markdown]
# Data.
# %% [codecell]
string1 = "Fairy tales"
string2 = "rAil safety"
string3 = "Madam Curie"
string4 = "RadiOum came"

string5 = "William Shakespeare"
string6 = "I45am-a+weakish_speller"

# %% [codecell]
def gbxxi_solution(text1, text2):

    text1_list = [letter.lower() for letter in text1 if letter.isalpha()]
    text2_list = [letter.lower() for letter in text2 if letter.isalpha()]

    text1_list.sort()
    text2_list.sort()
    return text1_list == text2_list

# %% [codecell]
def lucidprogramming_solution1(text1, text2):
    ''' Prequisite that no sumbols are in our strings.
        Requires n log n time (since any comparison based sorting algorithm
        requires n log n time to sort).
        '''

    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()

    return (sorted(text1) == sorted(text2))

def lucidprogramming_solution2(text1, text2):
    ''' Prequisite that no sumbols are in our strings.'''

    # Preproccess.
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    # Hash table.
    hash_table = dict()

    if len(text1) != len(text2):
        return False

    # Hash table entries conditionals.

    for letter in text1:
        if letter in hash_table:
            hash_table[letter] += 1
        else:
            hash_table[letter] = 1

    for letter in text2:
        if letter in hash_table:
            hash_table[letter] -= 1
        else:
            hash_table[letter] = 1

    # Checking if our hash table has 0 in all it's elements.

    for element in hash_table:
        if hash_table[element] != 0:
            return False
    return True



# %% [markdown]
# Tests
# %% [codecell]
print(gbxxi_solution(string1, string2), "gbxxi_solution")
print(gbxxi_solution(string3, string4), "gbxxi_solution")
print(gbxxi_solution(string5, string6), "gbxxi_solution")
print(lucidprogramming_solution1(string1, string2), "lucidprogramming_solution1")
print(lucidprogramming_solution1(string3, string4), "lucidprogramming_solution1")
print(lucidprogramming_solution2(string1, string2), "lucidprogramming_solution2")
print(lucidprogramming_solution2(string3, string4), "lucidprogramming_solution2")

# %% [markdown]
# Given a string, develop an algorithm to return if it's a palindrome.

# %% [markdown]
# Data
# %% [codecell]
string = ["Was it a cat I saw?", "Νίψων ανομήματα μη μόναν ώψιν", 
            "Are we not drawn onward to new era?"]
# %% [markdown]
# Linear Time, Linear Space solution.
# %% [codecell]
for element in string:
    element = "".join([i for i in element if i.isalpha()]).lower()
    print(element == element[::-1])

# %% [markdown]
# Linear Time, solution.
# %% [codecell]
def is_palindrome(string):
    i = 0
    j = len(string) -1

    while i < j:
        while not string[i].isalnum() and i<j:
            i += 1
        while not string[j].isalnum() and i<j:
            j -= 1
        if string[i].lower() != string[j].lower():
            # print(f'The differnce is {string[:(i+1)]}, on character: {string[j]})
                                            # Personal note to see which 
                                            # character is different.
            return False
        i += 1
        j -= 1
    return True

# %% [codecell]
for element in string:
    print(is_palindrome(element))
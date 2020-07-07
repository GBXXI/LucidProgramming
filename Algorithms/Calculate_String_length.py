
# %% [markdown]
# Given a string, calculate its length recursively. 
# %% [markdown]
# Data.
# %% [codecell]
strings = ["GeorgeBitsonis", "TheofanisBitsonis", "SophiaBistoni"]

# %% [markdown]
# Iterative search.
# %% [codecell]
def iterative_string_length(string_):
    counter = 0
    for letter in string_:
        counter += 1
    return f"The length of the string is: {counter} characters long."
# %% [markdown]
# Recursive search.
# %% [codecell]
def recursive_string_length(string_):
    if string_ == "":
        return 0
    return 1 + recursive_string_length(string_[1:])
# %% [markdown]
# Testing.
# %% [codecell]
for i in strings:
    print(iterative_string_length(i))
    print(recursive_string_length(i))

# %% [markdown]
# Given a string, develop an algorithm to return the first occurring uppercase letter. We require both an iterative and recursive solution to this problem. 

# %% [markdown]
# Data.
# %% [codecell]
strings = ["GeorgeBitsonis","Georgebitsonis","georgebitsonis", "georgeBitsonis"]

# %% [markdown]
# Linear search.
# %% [codecell]
def find_uppercase_iterative(string_):
    for i in range(len(string_)):
        if string_[i].isupper():
            return string_[i]
    return "No uppercase character."

# %% [markdown]
# Recursive search.
# %% [codecell]
def find_uppercase_recursive(string_, idx=0):
    if string_[idx].isupper():
        return string_[idx]
    if idx == len(string_) -1:
        return "No uppercase character."
    return find_uppercase_recursive(string_, idx+1)

# %% [markdown]
# Alternative Recursive Search.
# %% [codecell]
def find_uppercase_recursive_alternative(string_):
    if len(string_) == 0:
        return "No upper case character."
    if string_[0].isupper():
        return string_[0]
    else:
        return find_uppercase_recursive_alternative(string_[1:])


# %% [markdown]
# Testing.
# %% [codecell]
for element in strings:
    print(find_uppercase_iterative(element), f"Element, {element}")
    print(find_uppercase_recursive(element), f"Element, {element}")
    print(find_uppercase_recursive_alternative(element), f"Element, {element}")
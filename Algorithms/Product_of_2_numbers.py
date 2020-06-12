
# %% [markdown]
# Given two numbers, find their product using recursion.

# %% [markdown]
# Data.
# %% [codecell]
x = 5
y = 3

# %% [codecell]
def recursive_multiply(x, y):

    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

# %% [codecell]
print(recursive_multiply(x, y))
print(recursive_multiply(4, 5))
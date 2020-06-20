
# %% [markdown]
# Binary Search algorithm in Python.<br>
# Binary Search is a technique that allows you to search an ordered list of 
# elements very efficiently using a divide-and-conquer strategy

# %% [markdown]
# Data
# %% [codecell]
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 25

# %% [markdown]
# Linear Search.
# %% [codecell]
def linear_search(data, target):
    for i in range (len(data)):
        if data[i] == target:
            return True
    return False

# %% [markdown]
# Iterative Binary Search.
# %% [codecell]
def dinary_search_iterative(data, target):     
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high)  // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# %% [markdown]
# Recursive Binary Search.
# %% [codecell]
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


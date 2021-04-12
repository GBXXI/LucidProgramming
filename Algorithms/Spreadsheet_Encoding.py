
# %% [markdown]
# Implement a function that converts a spreadsheet column ID (i.e. "A", "B",
# "C", ..., "Z", "AA", etc.) to the corresponding integer.

# %% [markdown]
# Dataset.
# %% [codecell]
dataset = {
        "A": 1 ,
        "B": 2 ,
        "C": 3 ,
        "D": 4 ,
        "E": 5 ,
        "F": 6 ,
        "G": 7 ,
        "H": 8 ,
        "I": 9 ,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }

# %% [markdown]
# Personal solution, WRONG!!!
# Works only for sigle or double character cells.
# %% [codecell]
def tranform(cell, dataset):
    
    shifter = 0
    if len(cell) <= 1:
        return(dataset[f'{cell.upper()}'])
    else:
        for _ in cell[0:-1]:
            shifter += dataset['Z'] * dataset[f'{_.upper()}']
        return(f'{shifter + dataset[f"{cell[-1].upper()}"]}')

# %% [codecell]
def transform_base26(cell, dataset):
    base = 0
    n = len(cell) -1

    for _ in cell:
        base += pow(26,n) * dataset[f'{_.upper()}'] 
        n -= 1
    return base

# %% [codecell]
if __name__ == "__main__":
    test_list = [
        'aa',
        'ZZ',
        'ab',
        'Ac',
        'Ca',
        'K',
        'Kna',
        'lk',
        'p',
        'ap',
        'amj'
    ]
    
    for element in test_list:
        print(transform_base26(element, dataset))
        print(tranform(element, dataset))
        print(f'test: {element} \n')
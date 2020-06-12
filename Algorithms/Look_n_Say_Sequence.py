
# %% [markdown]
# ## String Processing: Look and Say Sequence.<br>

# The sequence starts with the number 1:<br>
#                1<br>
# We then say how many of each integer exists in the sequence to 
# generate the next term.<br>
# For instance, there is "one 1". This gives the next term:<br>
#                1<br>
#                11<br>
#                21<br>
#                12 11<br>
#                11 12 21<br>
#                31 22 11<br>
#                13 11 22 21<br>
# More information on:<br>
# <link>https://en.wikipedia.org/wiki/Look-and-say_sequence</link>

# %% [codecell]
def lns_seq(seq):
    occ_list = []
    i = 0
    while i < len(seq):
        count = 1
        while i + 1 < len(seq)   and seq[i] == seq[i+1]:
           i += 1
           count += 1
        occ_list.append(str(count)+seq[i])
        i += 1
    return "".join(occ_list)

# %% [codecell]
def first_elem_rept(first_element, repetion):
    s = first_element
    for _ in range(repetion-1):
        s = lns_seq(s)
    print(f'{str(first_element)} + {s}')
    return print(s)

# %% [codecell]
s = "1211"    
lns_seq(s)
first_elem_rept("d", 5)
        
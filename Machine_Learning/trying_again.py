trying_again.py


data_17 = pd.read_csv("/Users/user/Downloads/mongodb-database-tools-macos-x86_64-100.5.4/bin/Section8-FY17.csv")
data_22 = pd.read_csv("/Users/user/Downloads/mongodb-database-tools-macos-x86_64-100.5.4/bin/Section8-FY22.csv")

import pandas as pd
import numpy as np
import functools
from sqlalchemy import column

try22.head()


try_17 = data_17.pop('cbsasub')
len(try_17)
type(try_17)

try22 = data_22.pop('cbsasub')
len(try22)
# pd.Series.str.split(try22)

new_17 = try_17.tolist()
print(type(new_17))

new_22 = try22.tolist()
print(type(new_22))

print(new_22[0:6])
drp_ls = []
# for items in new_17 and new_22:

i = np.iterable
for row in new_17:
    if row in new_17 not in new_22:
        new_22.remove(row)



print(newer_17)
len(newer_17)
        
    

matched_values = try_17[column][try_17[column]]==try22[column]
print(matched_values)

# using map() + reduce() to check if 
# lists are equal
# if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, new_17, new_22), True) : 
#     print ("The lists are identical")
# else :
#     print ("The lists are not identical")


# def non_match_elements(new_17, new_22):
#     non_match = []
#     for i in new_17:
#         if i not in new_22:
#             non_match.append(i)
#     return non_match
       

# non_match = non_match_elements(new_17, new_22)
# print("No match elements: ", non_match)    

# def get_difference(new_17, new_22):
#     return set(new_17)-set(new_22)

# non_match = list(get_difference(new_17, new_22))
# print("No match elements: ", non_match)

def get_difference(new_17, new_22):
    non_match_a  = set(new_17)-set(new_22).remove()
    non_match_b  = set(new_22)-set(new_17).remove()
    non_match = list(non_match_a) + list(non_match_b)
    return non_match



non_a = list(non_match_a)
print(non_a)
len(non_a)


non_match = get_difference(new_22,new_17)
print("Non-match elements: ", non_match)

non_match_a  = set(new_17)-set(new_22)
non_a = non_match_a.pop()
type(non_match_a)
df = non_match_a
len(df)
print(df)


for i in non_match and data_17:
    print(data_17.pop(i))

data_17.pop(i)
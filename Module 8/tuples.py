numbers = (1, 2, 3, 4)

x = (1,2,3)
3 in x # True
x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

first_tuple = (1, 2, 3, 3, 3)

first_tuple[1] // 2
first_tuple[2] // 3
first_tuple[-1] // 3

second_tuple = tuple(5, 1, 2)

second_tuple[0] # 5
second_tuple[-1] # 2

names = ('Colt', 'Blue', 'Rusty', 'Lassie')

for name in names:
    print(name)

# Colt
# Blue
# Rusty
# Lassie

x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned

# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5, "a"}

4 in s
# True

8 in s
# False


numbers = {1,2,3,4}

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4

s = set([1, 2, 3])

s.add(4)

s # {1, 2, 3, 4}

s.add(4)

s # {1, 2, 3, 4}

set1 = {1,2,3,4,5,6}

set1.remove(3)

print(set1) # {1, 2, 4, 5, 6}

s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

s = set([1, 2, 3])

s.clear()

s # set()

{x**2 for x in range(10)}

# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

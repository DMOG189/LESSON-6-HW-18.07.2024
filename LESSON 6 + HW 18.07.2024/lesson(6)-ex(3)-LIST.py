# LESSON 6 EX 3 LIST

# START

numbers: list[int] = [10, 2, -1, 4]
more_numbers: list[int] = [99, -999]

# add list 2 to list 1
numbers.extend(more_numbers)
print(numbers)
print(more_numbers)
print("after concat", numbers)

# remove first occurrence
x = numbers.remove(-999)
print(x)
print("after remove 999", numbers)

# last index
pop: int = numbers.pop()
print("pop", pop)
print("after pop", numbers)

# last index
pop2: int = numbers.pop(1)
print("pop index [1] ==", pop2)
print("after pop [1]", numbers)

# del function
del numbers[1] # removes index 1
print("after remove item index 1", numbers)

# how to remove all occurrence of 99?
while 99 in numbers:
    numbers.remove(99)

# clear
numbers.clear()
print("after clear", numbers)

# extend
# A:
numbers.extend([10, 2, -1, 4])
print("after extend", numbers)
print("numbers.index(-1)", numbers.index(-1))
# B:
numbers.extend([4, 4, 4, 4, 4])
print("after extend", numbers)
print("numbers.index(4)", numbers.index(4))

# copy
clone = numbers.copy()

# sort (changes the list)
clone.sort()
print("after sort[clone]", clone)

# reverse sorting
clone.sort(reverse=True)
print("after sort revers [clone]", clone)
print("after reversed", reversed(numbers))

# iterator
print("after reversed", list(reversed(numbers)))

# sort (does NOT change the list)
print("after sorted", sorted(numbers))
print("after sorted reverse", sorted(numbers, reverse=True))
print(numbers)

# ALL FUNTION
bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[bool] = [20, 0, 300, 100, 100]
print("all bool1", bool1, all(bool1)) # True
print("all bool2", bool2, all(bool2)) # False
print("all bool3", bool3, all(bool3)) # True

# ANY FUNTION
bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[bool] = [20, 0, 300, 100, 100]
bool4: list[bool] = [True, False]
bool5: list[bool] = [0, 0, 0, 0, 0]
print("any bool1", bool1, any(bool1)) # True
print("any bool2", bool2, any(bool2)) # True
print("any bool3", bool3, any(bool3)) # True
print("any bool4", bool4, any(bool4)) # True
print("any bool5", bool5, any(bool5)) # False

# END
# LESSON 6 EX 4 COMPREHENSION

# make this list in a loop using append and COMPREHENSION
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# START

# using append
squares = []

for i in range(10):
    squares.append(i * i)

print(squares)


# using list comprehension
squares = [i * i for i in range(10)]

print(squares)

# END



# START

# method learned in class

# append
n_list: list[int] = []
for i in  range(0, 10):
    n_list.append(i ** 2);
print(n_list);

# comprehension
#         what to append ?  for-loop
n_list: list[int] = [i ** 2 for  i in range(10)]
print(n_list);

# END
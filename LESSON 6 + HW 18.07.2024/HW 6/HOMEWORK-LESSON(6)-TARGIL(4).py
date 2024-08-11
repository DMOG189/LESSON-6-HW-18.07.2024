# HOMEWORK-LESSON 6 TARGIL 4

# COMPREHENSION LIST
# 1.In one line - create a list of numbers from 95 to 105
# 2.In one line - create a list of even numbers from 10 to 20
# 3.In one line - create a list of 5 random True/False values
# 4.When should a memory cell be named _? Why does it help readability?
# 5.In one line - create a list of 10 random numbers between 1 and 100
# 6.In one line - from the list created in the previous section, create a list containing only the numbers greater than 50
# 7.Bonus: Can you combine the previous two sections in one line?
# 8.Bonus: Get strings from the user. In one line, create a list containing all the letters the user entered except for the letter 't' and spaces.

# START

import random

# 1.In one line - create a list of numbers from 95 to 105
numbers_95_to_105 = [x for x in range(95, 106)]
print("Numbers from 95 to 105:", numbers_95_to_105)

# 2.In one line - create a list of even numbers from 10 to 20
even_numbers_10_to_20 = [x for x in range(10, 21) if x % 2 == 0]
print("Even numbers from 10 to 20:", even_numbers_10_to_20)

# 3.In one line - create a list of 5 random True/False values
random_bools = [random.choice([True, False]) for _ in range(5)]
print("Random True/False list:", random_bools)

# 4.When should a memory cell be named _? Why does it help readability?
# The variable `_` is commonly used as a placeholder name in loops, comprehensions, or when the value is not needed.
# It improves readability by indicating that the variable's value is not important or will not be used.

# 5.In one line - create a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("10 random numbers between 1 and 100:", random_numbers)

# 6.In one line -
# from the list created in the previous section, create a list containing only the numbers greater than 50
numbers_greater_than_50 = [x for x in random_numbers if x > 50]
print("Numbers greater than 50:", numbers_greater_than_50)

# 7.Bonus: Can you combine the previous two sections in one line?
numbers_greater_than_50_direct = [x for x in [random.randint(1, 100) for _ in range(10)] if x > 50]
print("Combined: Numbers greater than 50 from 10 random numbers:", numbers_greater_than_50_direct)

# 8.Bonus: Get strings from the user. In one line,
# create a list containing all the letters the user entered except for the letter 't' and spaces.
user_input = input("Enter strings: ")
filtered_chars = [char for char in user_input if char != 't' and char != ' ']
print("Filtered characters (excluding 't' and spaces):", filtered_chars)

# END
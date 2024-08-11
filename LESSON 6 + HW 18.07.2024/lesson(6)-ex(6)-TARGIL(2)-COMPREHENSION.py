# LESSON 6 EX 6 TARGIL 2 COMPREHENSION

# use comprehension to build a list with 10 random numbers between 10 and 100

# START

import random

random_numbers = [random.randint(10, 100) for _ in range(10)]

print(random_numbers)

# END
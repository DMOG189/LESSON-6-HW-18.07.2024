# LESSON 6 EX 7 TARGIL 3 COMPREHENSION

# use comprehension to build a list with 10 random numbers between 1-100
# use only even numbers, do not include odd numbers
# the list may not be in 10 length

# START

# my solution
import random

random_even_numbers = [num for num in (random.randint(1, 100) for _ in range(10)) if num % 2 == 0]

print(random_even_numbers)

# END


# START

# the way learned

rand_even: list[int] =[]
for i in range(10):
    rnd: int = random.randint(1, 100)
    if rnd % 2 ==0:
        rand_even.append(rnd)

targil3_1: list[int] = [random.randint(1, 100) for _ in range(10)]
targil3_2: list[int] = [n for n in targil3_1 if n % 2 == 0]

print(targil3_2)

# one line ! crazy
crazy: list[int] = [num for num in [random.randit(1, 100) for _ in range(10) if num % 2 == 0]
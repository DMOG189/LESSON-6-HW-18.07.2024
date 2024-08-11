# HOMEWORK-LESSON 6 TARGIL 3

# BOOL LIST
# 1.Create a list with 3 elements and populate it with random values of False or True using random.choice
# 2.In one operation, check and print if the entire list contains only True
# 3.In one operation, check and print if the list contains at least one True
# 4.In one operation, check and print if the entire list contains only False
# 5.In one operation, check and print if the list contains at least one False
# 6.Create a random list of five numbers between -2 and 2 (including -2, -1, 0, 1, 2) using random
# 7.In one operation, check and print if the entire list contains only non-zero numbers
# 8.In one operation, check and print if the list contains at least one non-zero number
# 9. In one operation, check and print if the entire list contains only zeros
# 10. In one operation, check and print if the list contains at least one zero

# START

import random

# 1.Create a list with 3 elements and populate it with random values of False or True using random.choice
bool_list = [random.choice([True, False]) for _ in range(3)]
print("Boolean List:", bool_list)

# 2.In one operation, check and print if the entire list contains only True
all_true = all(bool_list)
print("All elements are True:", all_true)

# 3.In one operation, check and print if the list contains at least one True
at_least_one_true = any(bool_list)
print("At least one element is True:", at_least_one_true)

# 4.In one operation, check and print if the entire list contains only False
all_false = all(not x for x in bool_list)
print("All elements are False:", all_false)

# 5.In one operation, check and print if the list contains at least one False
at_least_one_false = any(not x for x in bool_list)
print("At least one element is False:", at_least_one_false)

# 6.Create a random list of five numbers between -2 and 2 (including -2, -1, 0, 1, 2) using random
number_list = [random.randint(-2, 2) for _ in range(5)]
print("Number List:", number_list)

# 7.In one operation, check and print if the entire list contains only non-zero numbers
all_non_zero = all(x != 0 for x in number_list)
print("All elements are non-zero:", all_non_zero)

# 8.In one operation, check and print if the list contains at least one non-zero number
at_least_one_non_zero = any(x != 0 for x in number_list)
print("At least one element is non-zero:", at_least_one_non_zero)

# 9. In one operation, check and print if the entire list contains only zeros
all_zero = all(x == 0 for x in number_list)
print("All elements are zero:", all_zero)

# 10. In one operation, check and print if the list contains at least one zero
at_least_one_zero = any(x == 0 for x in number_list)
print("At least one element is zero:", at_least_one_zero)

# END
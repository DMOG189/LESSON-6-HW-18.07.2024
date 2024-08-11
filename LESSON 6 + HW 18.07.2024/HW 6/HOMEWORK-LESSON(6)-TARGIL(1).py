# HOMEWORK-LESSON 6 TARGIL 1

# list exercise
# 1.create an empty list and enter the numbers between 80-99 in a for loop using append
# 2.print the first part of the list (clue: index 0)
# 3.print the last part of the list (clue: index -1)
# 4.print how many parts are in the list
# 5.print index 3 to 12 included 12
# 6.print index 3 to the end of the list
# 7.print the list till index 9
# 8.enter the number 999 in the center of the list
# 9.print the list backwards
# 10.print the list only for odd index

# START

# 1.create an empty list and enter the numbers between 80-99 in a for loop using append
numbers_list = []
for number in range(80, 100):
    numbers_list.append(number)

# 2.print the first part of the list (clue: index 0)
print(numbers_list[0])

# 3.print the last part of the list (clue: index -1)
print(numbers_list[-1])

# 4.print how many parts are in the list
print(len(numbers_list))

# 5.print index 3 to 12 included 12
print(numbers_list[3:13])

# 6.print index 3 to the end of the list
print(numbers_list[3:])

# 7.print the list till index 9
print(numbers_list[:10])

# 8.enter the number 999 in the center of the list
middle_index = len(numbers_list) // 2
numbers_list.insert(middle_index, 999)
print(numbers_list)

# 9.print the list backwards
print(numbers_list[::-1])

# 10.print the list only for odd index
print(numbers_list[1::2])

# END
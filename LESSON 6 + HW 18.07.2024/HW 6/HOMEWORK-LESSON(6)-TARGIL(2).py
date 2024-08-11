# HOMEWORK-LESSON 6 TARGIL 2

# EMPTY LIST
# 1.Create an empty list of decimal numbers for temperatures
# 2.Get temperatures from the user until the number -999 is entered.
# Each temperature entered should be added to the list.
# Do not add a temperature greater than 50 or less than -50
# 3.Add the following temperature list to the end of the current list: [18.5, 39.1, -20.0]
# 4.Print the highest temperature (hint: use max)
# 5.Print the lowest temperature (hint: use min)
# 6.Print the average temperature using sum and len
# 7.Print the average temperature using mean (from the statistics library)
# 8.Remove the temperature at index 0 (hint: use del)
# 9.Remove the temperature 18.5 (hint: use remove)
# 10.Pop the last temperature in the list into a variable called last_temp (hint: use pop)
# 11.Duplicate the list using copy, then sort the new list you created
# 12.Duplicate the list again using copy, then sort the new list in reverse order
# 13.What is the difference between sort and sorted?
# 14.What type does the reversed function return? How can you convert it to a list?

# START

import statistics

# 1.Create an empty list of decimal numbers for temperatures
temperatures = []

# 2.Get temperatures from the user until the number -999 is entered.
# Each temperature entered should be added to the list.
# Do not add a temperature greater than 50 or less than -50
while True:
    temp = float(input("Enter a temperature (enter -999 to stop): "))
    if temp == -999:
        break
    if -50 <= temp <= 50:
        temperatures.append(temp)

# 3.Add the following temperature list to the end of the current list: [18.5, 39.1, -20.0]
new_temperatures = [18.5, 39.1, -20.0]
temperatures.extend(new_temperatures)

# 4.Print the highest temperature (hint: use max)
print("The highest temperature:", max(temperatures))

# 5.Print the lowest temperature (hint: use min)
print("The lowest temperature:", min(temperatures))

# 6.Print the average temperature using sum and len
print("Average temperature (method 1):", sum(temperatures) / len(temperatures))

# 7.Print the average temperature using mean (from the statistics library)
print("Average temperature (method 2):", statistics.mean(temperatures))

# 8.Remove the temperature at index 0 (hint: use del)
del temperatures[0]

# 9.Remove the temperature 18.5 (hint: use remove)
temperatures.remove(18.5)

# 10.Pop the last temperature in the list into a variable called last_temp (hint: use pop)
last_temp = temperatures.pop()

# 11.Duplicate the list using copy, then sort the new list you created
sorted_temperatures = temperatures.copy()
sorted_temperatures.sort()

# 12.Duplicate the list again using copy, then sort the new list in reverse order
reverse_sorted_temperatures = temperatures.copy()
reverse_sorted_temperatures.sort(reverse=True)

# 13.What is the difference between sort and sorted?
# - The sort function sorts the original list and saves the changes.
# - The sorted function returns a new list that is a sorted version of the original list without modifying it.

# 14.What type does the reversed function return? How can you convert it to a list?
# The reversed function returns a reversed object.
# To convert it into a list, you can use the list() function like this:
# list(reversed(temperatures))

# END
# LESSON 6 EX 1 LIST

# LIST

# START

# INDEX:              0   1   2  3  len = 4
numbers: list[int] = [10, 2, -1, 4]
#                    200, 201, 202, 203
#   numbers == 200
#   numbers[1]
print(numbers)
print(f"numbers[0] = {numbers[0]}") # 10
print(f"numbers[3] = {numbers[3]}") # 10
# print(numbers[4]) # ERROR

print(f"list length = {len(numbers)}")

# for: (use it when we need the index)
for i in range(0, len(numbers)):
    number = numbers[i]
    print(f"numbers[{i}] = {numbers[i]}", end=" | ") # 10

# for each:
for number in numbers:
    print(number, end=" ")

for c in "Hello":
    print(c, end="")
print()

# index

print(f"numbers[0: 3] = {numbers[0: 3]}") # numbers[0: 3] = [10, 2, -1]
print(f"numbers[:3] = {numbers[:3]}") # numbers[:3] = [10, 2, -1]
print(f"numbers[:] = {numbers[:]}") # numbers[:] = [10, 2, -1, 4]
print(f"numbers[2: 4] = {numbers[2: 4]}") # numbers[2: 4] = [-1, 4]
print(f"numbers[2:] = {numbers[2:]}") # numbers[2:] = [-1, 4]
print(f"numbers[0:4:2] = {numbers[0:4:2]}") # numbers[0:4:2] = [10, -1]
print(f"numbers[::-1] = {numbers[::-1]}") # numbers[::-1] = [4, -1, 2, 10]
print(f"numbers[len(numbers) -1] = {numbers[len(numbers) -1]}") # numbers[len(numbers) -1] = 4
print(f"numbers[-1] = {numbers[-1]}") # numbers[-1] = 4
print(f"numbers[-2] = {numbers[-2]}") # numbers[-2] = -1

print()
print("original", numbers)
numbers[0] = 200
print("after numbers[0] = 200", numbers)
numbers.insert(2, 444)
print("numbers.insert(2, 444)", numbers)
print()

# END
# HOMEWORK-LESSON 6 TARGIL 5

# ERROR HANDLING
# 1.Create a list of 4 numbers
# 2.Write a loop that takes numbers from the user until the user enters -999
# I: Print the list element at the index provided by the user
# II: Wrap the code with try-except to catch errors
# III: Handle if the user enters a non-integer value
# III: Handle if the user enters an index out of range

# START

# 1.Create a list of 4 numbers
numbers_list = [10, 20, 30, 40]

# 2.Write a loop that takes numbers from the user until the user enters -999
while True:
    try:
        user_input = input("Enter an index to retrieve the number (enter -999 to stop): ")
        index = int(user_input)
        if index == -999:
            break

        # I: Print the list element at the index provided by the user
        print(f"The number at index {index} is {numbers_list[index]}")

    # II: Wrap the code with try-except to catch errors
    except ValueError:
        # III: Handle if the user enters a non-integer value
        print("Error: Please enter a valid number.")
    # III: Handle if the user enters an index out of range
    except IndexError:
        print(
            f"Error: Index out of range. Please enter a number between 0 and {len(numbers_list) - 1}.")


# END
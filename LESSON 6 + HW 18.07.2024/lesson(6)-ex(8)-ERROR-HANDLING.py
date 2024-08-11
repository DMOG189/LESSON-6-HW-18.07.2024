# LESSON 6 EX 8 ERROR HANDLING

# ERROR HANDLING
# introduction


# START

# EXAMPLE introduction


numbers: list[int] = [1, 4, 5, 9]
# print(numbers[4])  # code error


# this may crash

try:
    grade: int = int(input("enter grade"))
    print("grade is ok")
except:
    print("something went wrong ... 404")



# if grade -- false

grade: int = None
while not grade:
    try:
        grade: int = int(input("enter grade"))
        print("grade is ok")
    except:
        print("something went wrong ... 404")


# this is how to print the error
e: Exception = ValueError
grade: int = None
while not grade:
    try:
        grade: int = int(input("enter grade"))
    except Exception as e:
        print(f"something went wrong --{e}--... try again")

print("finish")

# END
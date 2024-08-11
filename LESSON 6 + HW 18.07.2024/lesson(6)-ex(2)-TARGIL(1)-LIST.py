# LESSON 6 EX 2 TARGIL 1 LIST


# input grade from user until enter -999
# ignore < 0 or > 100
# store all of the grades in a list

# START

grades: list[int] = []
while True:
    grade: int = int(input("enter grade [-999 to exit]:"))
    if grade == -999:
        break
    if grade < 0 or grade > 100:
        continue
    grades.append(grade) # insert at the end

# OPTION A
print(grades)
print(f"max(grades) = {max(grades)}")
print(f"min(grades) = {min(grades)}")
print(f"sum(grades) = {sum(grades)}")
print(f"len(grades) = {len(grades)}")

# OPTION B
# print all in a single code line
print(f"sum(grades) = {sum(grades) / len(grades) / max(grades) / min(grades): .2f}")


# OPTION C
import statistics
print(f"sum(grades) = {statistics.mean(grades) : .2f}")


# END
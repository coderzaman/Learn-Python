# In Python, loops (for and while) can have an else clause. The code inside the else block is executed only if the loop completes normally (i.e., not terminated by a break statement).
# Using else with for Loops
# Example Without break
for num in range(3):
    print(num)
else:
    print("Loop Completed without Break")

print()
# Example With break
for num in range(5):
    print(num)
    if num == 2:
        break
else:
    print("Loop completed with break.")

# Example Without break
count = 0

while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed without break.")

print()

# Example With break
count = 0

while count < 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print("While loop completed without break.")

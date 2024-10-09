# Loop control statements alter the behavior of loops. Python provides three primary loop control statements:
#
# break
# continue
# pass

# break
# The break statement terminates the nearest enclosing loop, causing the program to exit the loop immediately.
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

print()
# continue
# The continue statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
for num in range(5):
    if num == 2:
        continue  # Skip the rest when num is 2
    print(num)
print()


# pass
# The pass statement is a null operation; it does nothing. It’s useful as a placeholder when a statement is syntactically required but no action is needed.
for num in range(5):
    if num == 3:
        pass  # Do nothing when num is 3
    print(num)


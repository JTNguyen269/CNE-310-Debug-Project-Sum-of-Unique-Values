def lone_sum(a, b, c):

# Find the sum of all three numbers, a, b, and c.

    total = a + b + c

# verify if all three values are the same. If the condition is true, then return 0.

    if a == b and a == c and b == c:
        return 0

# verify if there are any two values that are the same. If that is the case, return the third value.

    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a

# If none of those conditions are met, the sum of variables a, b, and c should be returned.

    return total

# Examples for testing purposes.

print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(10, 10, 10)))
print("lone_sum of 1, 2, 3 should be 6: " + str(lone_sum(1, 2, 3)))
print("lone_sum of 1, 2, 1 should be 2: " + str(lone_sum(1, 2, 1)))
print("lone_sum of 4, 5, 6 should be 15: " + str(lone_sum(4, 5, 6)))
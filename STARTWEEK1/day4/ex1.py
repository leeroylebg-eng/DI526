# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:

def calculation(a, b):
    # Your Code
    add = a + b
    sub = a - b
    return {'addition': add, 'subtraction': sub}

res = calculation(40, 10)
print(res)
# 1
print([x for x in [1,2,3,4]])

# 2
print([x * 20 for x in [1,2,3,4]])

# 3
print([name[0] for name in ["Elie", "Tim", "Matt"]])

# 4
print([x for x in [1,2,3,4,5,6] if x % 2 == 0])

# 5
print([x for x in [1,2,3,4] if x in [3,4,5,6]])

# 6
print([word[::-1].lower() for word in ["Elie", "Tim", "Matt"]])

# 7
print("".join([c for c in "first" if c in "third"]))

# 8
print([x for x in range(1,101) if x % 12 == 0])

# 9
print([c for c in "amazing" if c not in "aeiou"])

# 10
print([[x for x in range(3)] for _ in range(3)])

# 11
print([[x for x in range(10)] for _ in range(10)])

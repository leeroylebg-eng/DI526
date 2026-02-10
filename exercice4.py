# 1
[x for x in [1,2,3,4]]

# 2
[x * 20 for x in [1,2,3,4]]

# 3
[name[0] for name in ["Elie", "Tim", "Matt"]]

# 4
[x for x in [1,2,3,4,5,6] if x % 2 == 0]

# 5
[x for x in [1,2,3,4] if x in [3,4,5,6]]

# 6
[word[::-1].lower() for word in ["Elie", "Tim", "Matt"]]

# 7
"".join([c for c in "first" if c in "third"])

# 8
[x for x in range(1,101) if x % 12 == 0]

# 9
[c for c in "amazing" if c not in "aeiou"]

# 10
[[x for x in range(3)] for _ in range(3)]

# 11
[[x for x in range(10)] for _ in range(10)]

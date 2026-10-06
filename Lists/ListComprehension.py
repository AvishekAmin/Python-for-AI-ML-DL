# Without using list comprehension
squares = []

for i in range(6):
    if i%2 == 0:
        squares.append(i*i)

# With using list comprehension
# Problem 1
print(squares)

sq = [i*i for i in range(6) if i%2 == 0]
print(sq)

# Problem 2
nums = [-2, -3, 3, 4, -1, 7]

nums = [0 if val < 0 else val for val in nums]
print(nums)

# Problem 3
words = ["hello", "python", "avishek"]

words = [val.upper() for val in words]
print(words)
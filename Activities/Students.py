info = [
    ("Anup", "Math"),
    ("Bhuvan", "Science"),
    ("Anup", "Science"),
    ("Chayan", "Math"),
    ("Bhuvan", "Math"),
    ("Anup", "English"),
    ("Chayan", "English"),
]

# 1. Print all unique courses

# courses_set = set()

# for tup in info:
#     courses_set.add(tup[1])

# print(courses_set)

# 2. Create dictionary (student, set of courses)

dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
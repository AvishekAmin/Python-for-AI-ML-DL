marks = [88, 98, 93, 95, 100]

marks.append(94)
print(marks)        # [88, 98, 93, 95, 100, 94]

marks.insert(3,92)
print(marks)        # [88, 98, 93, 92, 95, 100, 94]

marks.sort()
print(marks)        # [88, 92, 93, 94, 95, 98, 100]

marks.reverse()
print(marks)        # [100, 98, 95, 94, 93, 92, 88]

marks.remove(98)
print(marks)        # [100, 95, 94, 93, 92, 88]

num = [1, 2, 3, 4, 5]
num.sort(reverse=True)
print(num)          # [5, 4, 3, 2, 1]
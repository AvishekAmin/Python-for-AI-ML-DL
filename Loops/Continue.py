# Print 1, 2, 3 -> skip, 4, 5, 6 -> skip, 7, 8, 9 -> skip, 10
i = 1
while (i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1
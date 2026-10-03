n1 = int(input("Enter number of list 1 items: "))
list1 = []

print(f"Enter {n1} numbers:")
for num in range(n1):
    list1.append(int(input()))

n2 = int(input("Enter number of list 2 items: "))
list2 = []

print(f"Enter {n2} numbers:")
for num in range(n2):
    list2.append(int(input()))

list3 = list1 + list2
list3.sort()

print(f"After merging and sorting: {list3}")
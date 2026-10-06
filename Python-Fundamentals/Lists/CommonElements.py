n1 = int(input("Enter number of list 1 items: "))
list1 = []

print(f"Enter {n1} elements:")
for num in range(n1):
    list1.append(int(input()))

n2 = int(input("Enter number of list 2 items: "))
list2 = []

print(f"Enter {n2} numbers:")
for num in range(n2):
    list2.append(int(input()))

def is_common(list1, list2):
    return len(set(list1) & set(list2)) > 0

if(is_common(list1, list2)):
    print(f"{list1} and {list2} have common elements")
else:
    print(f"{list1} and {list2} have no common elements")
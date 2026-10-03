text = input("Enter a string: ")

def is_palindrome(text):
    start = 0
    end = len(text)-1

    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True

if is_palindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
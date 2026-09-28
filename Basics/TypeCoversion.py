# Type Conversion

ans = 5 + 10.0
print(ans)          # 15.0
print(type(ans))    # Float

# Type Casting

a = 5.2
b = int(a)
print(b)            # 5
print(type(b))      # Int

val = int("123")
print(type(val))    # Int

p = bool(10)
print(p)            # True (0 -> False, Every non-zero number -> True)
print(type(p))      #Bool
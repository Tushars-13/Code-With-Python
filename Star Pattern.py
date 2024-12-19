print()
print("------------------------------------------------------")
print()

print("Square star pattern")
a = 5
for i in range(a):
    for j in range(a):
        print("*", end=" ")
    print()

print()
print("------------------------------------------------------")
print()

print("Right triangle star pattern")
b = 5
for i in range(a):
    for j in range(i+1):
        print("*", end=" ")
    print()

print()
print("------------------------------------------------------")
print()

print("Inverted Right triangle star pattern")
c = 5
for i in reversed(range(c+1)):
    for j in range(i):
        print("*", end=" ")
    print()

print()
print("------------------------------------------------------")
print()


print("pyramid star pattern")
d = 5
for i in range(d):
    for j in range(d-i-1):
        print(" ",end="")
    for k in range(2 * i+1):
        print("*", end="")
    print()

print()
print("------------------------------------------------------")
print()

print("Diamond star pattern")
e = 5

# Upper part of the diamond
for i in range(e):
    print(" " * (e - i - 1) + "*" * (2 * i + 1))

# Lower part of the diamond
for i in range(e - 2, -1, -1):
    print(" " * (e - i - 1) + "*" * (2 * i + 1))
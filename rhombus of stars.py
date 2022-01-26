a = int(input("Enter the number of rows:"))
for i in range(1, a):
    print(" "*(a-i), "* "*(i))

for i in range(a-1, -1, -1):
    print(" "*(a-i), "* "*(i))
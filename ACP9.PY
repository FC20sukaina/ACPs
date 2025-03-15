a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter your third number : "))

print("Before swapping:")
print("a = {}, b = {}, c = {}".format(a,b,c))

a, b, c = c, b, a
print("After swapping:")
print("a = {}, b = {}, c={}".format(a,b,c))
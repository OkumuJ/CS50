from cs50 import get_int
x = get_int ("What's X? ")
y = get_int ("What's Y: ")

if x<y:
    print ("X is less than Y")
elif x>y:
    print ("X is greater than Y")
else:
    print ("X is equal to Y")
n = int(input("Enter the dividend"), 2)
d = int(input("Enter the divisor"), 2)
r = n
r = (r * 2) - d
for i in range(1,n-1):
    if r >= 0:
        q = 1
    elif r < 0:
        q = 0
print("quotient", bin(q))
print("remainder",bin(r))
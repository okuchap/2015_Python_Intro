# bisection search
x = int(raw_input("Enter an integer x:"))
y = abs(x)
epsilon = 0.01

low = 0
high = max(1.0, y)
ans = (low+high)/2.0

while abs((y-ans**2)) > epsilon:
    if ans**2 < y:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

if x>=0:
    print ans, "is close enough to square root of", x

else:
    print -ans, "is close enough to square root of", x

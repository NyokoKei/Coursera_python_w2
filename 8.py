a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
elif c == 0:
    y = f / d
    x = (e - b * y) / a
elif b == 0:
    x = e / a
    y = (f - d * y) / c
elif d == 0:
    x = f / c
    y = (e - a * x) / b
else:
    y = (f * a - e * c) / (d * a - b * c)
    x = (e - b * y) / a
print(x, y)

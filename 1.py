a, b, c = float(input()), float(input()), float(input())
s = (a + b + c) / 2
sq = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(sq)

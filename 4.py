x = input()
m, c = map(int, x.split('.'))
m += c // 100
c -= (c // 100) * 100
print(m, c)

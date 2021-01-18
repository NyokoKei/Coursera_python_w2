s = input()
i = s.find('f')
if i == -1:
    print(-2)
else:
    print(s.find('f', i + 1))

s = input()
i = s.find('f')
j = s.rfind('f')
if i != -1:
    if i == j:
        print(i)
    else:
        print(i, j)
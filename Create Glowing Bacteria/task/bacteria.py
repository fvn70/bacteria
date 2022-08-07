dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

first = input()
second = [dic[x] for x in first]
print(''.join(second))


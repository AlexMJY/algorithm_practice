s = str(input())
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    s = s.replace(i, 'a')
print(len(s)) 
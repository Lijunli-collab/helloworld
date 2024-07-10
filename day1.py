p = [1,2,3,4,5,6,7,8,9]
x = []

while len(p):
    x.append(p.pop())

for a in x:
    print(a,end='->')
print('NULL')

print(len(p))
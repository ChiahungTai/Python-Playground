print('Hello World')
x = ('S','T','U')
print(x)

(x, y) = (4, 'fred')
print(y)

a, b = (88, 98)
print(a, b)
print(('Jones', 'Sally') < ('Jones', 'Fred'))

d = {'a':10, 'b':1, 'c':22}
t = d.items()
print(t)
y = sorted(t)
print(y)

c = {'a':10, 'b':1, "c":22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp.sort(reverse = True)
print(tmp)
print("Test")
print(sorted([(v, k) for k, v in c.items()], reverse = False))


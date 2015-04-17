print('Hello World')

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
print("len of purse = ", len(purse))

jjj = {'chuck' : 1, 'fred':42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)

ccc = dict()
print('csev' in ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1
print(counts)

counts1 = dict()
for name in names:
    counts1[name] = counts1.get(name, 0) + 1
print(counts1)

for key in counts:
    print(key, counts[key])

print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

for aaa, bbb in jjj.items():
    print(aaa, bbb)


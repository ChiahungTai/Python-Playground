
print('Hello World')
fhand = open('mbox.txt')
print(fhand)

count = 0
for line in fhand:
    print(line, end='')
    count = count + 1
    if '@mozilla.com' in line:
        print("I got you!")
print('line count: ',  count)
fhand.close()

print('Please enter a filename:')
fname = input()
try:
    fhand = open(fname)
except:
    print('File can\'t be opened:', fname)
    exit()
inp = fhand.readlines()
print(len(inp))
for line in inp:
    line = line.rstrip()
    if not line.startswith('W'):
        continue
    print(line)


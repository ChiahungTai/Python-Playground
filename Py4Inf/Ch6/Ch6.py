print('Hello World')
fruit = 'banana'
x = len(fruit)
print(x)
index = 0
while(index < x):
    letter = fruit[index]
    print(letter)
    index = index +1
print("for ... in")
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count + 1
print('count = ', count)

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:30])
print(s[:2])
print(s[8:])
print(s[:])

print('n' in fruit)

word = 'monkey'
if word == 'banana':
    print("all right, banana")
if word < 'banana':
    print('your word ' + word + ' comes before banana')
elif word > 'banana':
    print('your word ' + word + ' comes after banana')
else:
    print("all right, banana")

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))

print(stuff.lower())
print(stuff.upper())
pos = fruit.find('na')
print(pos)

pos = fruit.find('z')
print(pos)

pos = fruit.rfind('na')
print(pos)

greet = 'Hello Bob'
print(greet.replace('Bob', 'Jane'))
print(greet.replace('o', 'X'))

greet = ' Hello Bob '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("P"))
print(line.startswith("p"))

data = "From stephen.marquard@uct.ca.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1:sppos]
print(host)


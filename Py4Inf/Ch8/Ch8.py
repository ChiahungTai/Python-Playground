print('Hello World')
print(['red', 23, 98.6])
print(1, [5, 6], 7)
numbers = ["1", '2', "3"]
print(numbers[1])
numbers[1] = 21
print(numbers[1])
print('len = ', len(numbers))
print(range(5))
friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print("Merry X'mas", friend)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

t = [9, 41, 132, 54, 78]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

x = list()
print(type(x))
print(dir(x))

x.append("book")
x.append("99")
x[1] = "ipod"
print(x)
x.append("cookies")
some = [1, 2, 55, 66, 77, 89]
print(77 in some)
print(1 not in some)

friends.sort()
print(friends)
print(friends[1])

print(max(some), min(some), sum(some), sum(some)/len(some))
words = "Show me the money"
stuff = words.split()
print(stuff)

words = "a lot of        space"
stuff = words.split()
print(stuff)

line = "first,second,third"
thing = line.split(',') 
print(thing)


print('Hello World')
while True:
    line = input('>');
    if '#' == line[0]:
        continue
    if line == 'done':
        break
    print(line)
print('Done')        

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

friends = ['ctai', 'john', 'peter']
for friend in friends:
    print(friend)
print('Done')

def largestNumber(list):
    largestSoFar = None
    for number in list:
        if largestSoFar is None:
            largestSoFar = number
        elif largestSoFar < number:
            largestSoFar = number
    return largestSoFar

def smallestNumber(list):
    smallestSoFar = None
    for number in list:
        if smallestSoFar is None:
            smallestSoFar = number
        elif smallestSoFar > number:
            smallestSoFar = number
    return smallestSoFar

listNumber = [9, 41, 12, 3, 74, 15]
print(largestNumber(listNumber))
print(smallestNumber(listNumber))
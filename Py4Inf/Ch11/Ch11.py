import re
print('Hello World')

test = "Hello I am comre from Taiwan"
print(re.search('from', test))

x = 'My two favorite numbers are 19 and 42'
print(re.findall('[0-9]+', x))
y = 'From: Using the : character'
print(re.findall('^F.+?:', y))


print('Ch2')

x=4
if x>2:
    print("Bigger")
else:
    print("Smaller")
print("All done")

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    ptint('Large')
print("All done")
x=3
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    ptint('Something else')

astr = 'How are you'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

x = 0

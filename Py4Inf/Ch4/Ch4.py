def hello():
    print('Hello World')
    print('Fun')

hello()
print("Zip")
hello()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

def greet():
    return 'Hello'

print(greet(), "Glenn")

def greet(lang):
    if lang == 'es':
        return('Hola')
    elif lang == 'fr':
        return('Bonjour')
    else:
        return('Hello')

print(greet('fr'), "Glenn")

def addTwo(a, b):
    added = a + b
    return added

print(addTwo(3, 5))


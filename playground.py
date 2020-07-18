a = 1
b = 'hello'
print(a)
print(b)

if a == 1 and (a == 1 or a == 1):
    print('hi')
    print('test')
    if a != 1:
        print('no')
elif a == 2:
    pass
else: 
    print('else!')

if a is not None:
    print('a isn\'t None')

if a:
    print('a')

if a is None:
    print('a is None')

def say():
    print('hi')

say()

# Prefer this
def say1(number):
    print(f'hi {number}')

# This is not recommended
def say2(number: int):
    print('hi ' + str(number))
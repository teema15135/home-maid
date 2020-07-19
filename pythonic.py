# Idiomatic Python code

# 1. Avoid comparing directly to `True`, `False`, or `None`

a = True
if a is True:
    print('a is True')

# Do this instead
if a:
    print('a is True')

# 2. Avoid repeating variable name in compound if statement

a = 1
if a == 1 or a == 2 or a == 3 or a == 4:
    print('a:', a)

# Do this instead
if a in [1, 2, 3, 4]:
    print('a:', a)

# 3. Use `in` to iterate over iterable

# Use this!!!!
l = [1, 2, 3, 4]
for item in l:
    print(item)

# 4. Use default parameter of `dict.get`

a = {
    'name': 'Teema'
}
if 'name' in a:
    print(a['name'])

# Do this instead
print(a.get('name', None))

# 5. Use `enumerate` function in loops

count = 1
name = ['T', 'EE', 'M', 'A']
for name in names:
    print(f'{count}. {name}')
    count += 1

# Do this instead

for index, name in enumerate(names):
    print(f'{index + 1}. {name}')
    count += 1

# 6. Use `_` for data that should be ignored

for _, name in enumerate(names):
    print(f'{name}')
    count += 1

# 7. Use (for) `else` after iterator is exhausted!

check = False
for name in names:
    if name == 'C':
        check = True
        break

if not check:
    print('C is not here')

# Do this instead
for name in names:
    # Do something
    pass
else:
    # If not happen `break` in for
    print('Yes')

# 8. List comprehension to craete a tranformed list

names = []
for i in range(10):
    names.append(i)

# Do this instead
names = [i for i in range(10)]

# 9. Use context manager to ensure resources are managed

f = open('test')
# do something
f.close()

# Do this
with open('test') as f:
    # do something

# 10. Use generator to lazily load infinite sequences

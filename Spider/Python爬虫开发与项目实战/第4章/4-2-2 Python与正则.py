import re

pattern = re.compile(r'\d+')

print('match:')
result1 = re.match(pattern, '192abc')
if result1:
    print(result1.group())
else:
    print('匹配失败 1')

result2 = re.match(pattern, 'abc192')
if result2:
    print(result2.group())
else:
    print('匹配失败 2')
print('-' * 50)


print('search:')
result1 = re.search(pattern, 'abc192edf')
if result1:
    print(result1.group())
else:
    print('匹配失败 1')
print('-' * 50)


print('split:')
print(re.split(pattern, 'A1B2C3D4'))
print('-' * 50)


print('findall:')
print(pattern.findall('A1B25C3D4'))
print('-' * 50)


print('finditer:')
matchiter = pattern.finditer('A1B25C3D4')
print(type(matchiter))
for match in matchiter:
    print(match.group())
print('-' * 50)


print('sub:')
p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
s = 'i say, hello world!'
print(p.sub(r'\g<word2> \g<word1>', s))
p = re.compile(r'(\w+) (\w+)')
print(p.sub(r'\2 \1', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(p.sub(func, s))
print('-' * 50)


print('subn:')


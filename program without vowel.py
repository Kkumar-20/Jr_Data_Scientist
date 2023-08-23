a = 'wavier the water'
b = ''
v = ['a', 'e', 'i', 'o', 'u']
for i in a:
    if not i in v:
        b = b + i
print('sentence = ', a)
print('sentence without vowel =', b)

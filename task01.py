text = ('salom dunyo')

c = 0

for i in text :
    if i.lower() in 'aioue':
        c += 1
        print(i)

print(c)
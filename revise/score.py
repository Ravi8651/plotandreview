animals = ['tiger', 'cat', 'dog']
am = animals.copy()
for a in am:
    if len(a) > 3:
        animals.append(a)
print(animals)

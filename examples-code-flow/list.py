# List example
l = [1, 2, 3, 4, 5, 'A', 'B']
l.append('C')
print(l)

# Tuple (immutable list) example
t = (1, 2, 3, 4, 5, 'A', 'B')
t.append('C') # Throws an error, since the list is immutable
print(t)

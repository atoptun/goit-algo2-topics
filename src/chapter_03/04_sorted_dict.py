from sortedcontainers import SortedDict

sd = SortedDict()
sd['c'] = 3
sd['a'] = 1
sd['b'] = 2
print(sd.keys())  # Виведе: ['a', 'b', 'c']

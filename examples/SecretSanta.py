import copy
from collections import OrderedDict, defaultdict
import random
import sys
import time

sys.path.append('../')

from Collections.Group import group
from Console.Printing import fake_loading_bars

print()
fake_loading_bars(0, 4, 80, 0.5, 'Booting')
print('*' * 80)
print('Welcome to Secret Santa Assignment Generator v12.25')
print()
print('Enter names for Secret Santa Assignment')
print('Enter a blank to continue and put couples on the same line.')

couples = defaultdict(list)
give = []

s = input()
while(s != ''):
    if len(s.split(' ')) > 1:
        split = s.split(' ')
        couples[split[0]] = [split[1]]
        couples[split[1]] = [split[0]]
        give.extend(split)
    else:
        give.append(s)
    s = input()

results = group(give, exclusion=couples)
    
fake_loading_bars(0, 4, 80, 0.5, 'Decorating Christmas Tree', 'Packing Sleigh', 'Baking Christmas Cookies', 'Making Toys')
print()
print('{:10}'.format('Giving'), '===', '{:>10}'.format('Receiving'))
print('-' * 25)
for k,v in results.items():
    print('{:10}'.format(k), '===', '{:>10}'.format(v[0]))
print()
print('*' * 80)
print()

# count => infinite counter (itertools)

from itertools import count

count1 = count() # infinite counter
range1 = range(10) # finite counter


print('rasge\n')
for i in range1:
    print(i)

print('\ncount\n')
for i in count1:
    print(i)
    if i >= 10:
        break


print(count1)
print(next(count1))
print(count1)

count2 = count(step=2, start=4)
range2 = range(4, 12, 2)

print('count2')
for i in count2:
    print(i)
    if i >= 10:
        break

print('range2')
for i in range2:
    print(i)

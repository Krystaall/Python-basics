# python built-in data structures are list,tuples,dictionary and sets

# 1. lists
list1 = []  # this is empty list
list2 = [1, 2, 'Sharvari']
print(list1)
print(list2)

# append
list1.append(1)
list1.append('me')
print(list1)

# extend
list1.extend((2, 0))
print(list1)

# difference between append and extend
list2.append((3, 4))  # appends as a tuple
list2.extend((3, 4))  # appends as single elements
print(list2)

# insert
list1.insert(1, 'mad')
print(list1)

# remove
list2.remove(3)
print(list2)

# difference between remove, del, pop
del list2[4]
print(list2)
a = list2.pop()
print(a)
print(list2)

# printing required elements
print(list1[2])   # if 1 required element
print(list1[0:3])  # print from given start index to given (end index-1) i.e. start:end
print(list1[0:3:2])  # print from start to end-1 skipping 2 elements i.e. start:end:skips


# reverse
list1.reverse()
print(list1)

# count
print(list1.count(1))

# can also use sort



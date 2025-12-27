#  Set is the collection of the unordered items.
#  we can not access set elements by using index numbers.
#  Each element in the set must be unique and immutable.
#  To create a set from scratch and directly add some elements to it, you can use curly braces.
#  Most important thing,remove duplicate values from the set.

element={1,2,3,4,4,4,'Hello','world','Hello'}
print(element)
# {1, 2, 3, 4, 'world', 'Hello'}
# see,here remove two 4 and one Hello.And also see,It's unordered.'world','Hello'.fist Hello remove.
print(type(element))
# <class 'set'>
print(len(element)) 

# Empty set
# when declare like this
product={}
print(type(product))
# <class 'dict'> . This is a dictionary.
# Then how do we declare an empty set?
product=set()
print(type(product))
# <class 'set'>
# so  if we need to declare an empty set,then use set function.


# add(el):-We can add in set.
product1=set()
product1.add(1)
product1.add('apple')
product1.add('2')
product1.add('banana')
product1.add((1,2,3,4))
print(product1)
# {'2', 1, (1, 2, 3, 4), 'apple', 'banana'}

# if I try to add list and dictionary in the set
# product1.add([1,2,'list'])
# print(product1) # It gives error like cannot use 'list' as a set element (unhashable type: 'list').
# hashing means where we can't change original value to another value.That means hash is immutable.

# remove(el):
pro2={1,2,3,'apple','banana'}
pro2.remove(2)
print(pro2)
# {1, 3, 'apple', 'banana'}
pro2.remove('apple')
print(pro2) # {1, 'banana', 3}


# clear():
pro3={1,2,3,"Orange",'mango','banana',(1,2,3,'apple')}
print(len(pro3))
# 7
pro3.clear()
print(len(pro3))
# 0
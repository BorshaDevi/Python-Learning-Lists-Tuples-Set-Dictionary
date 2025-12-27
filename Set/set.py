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


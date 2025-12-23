# Tuples is a built-in data type that lets us create immutable sequences of values.

# 1.A tuple is written using parentheses ().
# 2.If you give a single value like (1), it is not a tuple; it is treated as an integer. 
# To create a single-element tuple, you must add a comma, like(1,)

tup=()
print(type(tup))
# 'tuple'

tup1=(1)
print(tup1)
# 1
print(type(tup1))
# int

tup2=(1,)
print(tup2)
# (1,)
print(type(tup2))
# tuple

tup3=(1,2,3,4)
print(tup3[0])
# 1

# tup1[0]=9
# This operation is not allowed because tuples are immutable.

# Tuple slicing:
#  we can slice in tuple also.

tup4=(1,2,3,4,5,6,7)
print(tup4[1:3])
# (2, 3)

# Tuple method

# index():In this function,returns the first occurrence (first index) of the given value.

tup5=(1,2,1,3,4,5,2,6,5)
print(tup5.index(2))
# 1
print(tup5.index(1))
# 0
print(tup5.index(5))
# 5

# count():This counts total occurrences.

tup6=(1,2,1,3,4,5,2,6,5,2,9,7,2)
print(tup6.count(2))
# 4
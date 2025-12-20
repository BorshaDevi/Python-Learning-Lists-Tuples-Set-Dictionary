# 1. A built-in data type that stores a set of values.
list=[]
print(type(list))
# Class 'List'
print (len(list))
# 5

# Lists some property similar to string property.
# In string, we can go with a particular index and find the character, similar thinks we can do in List.
list1=[34,4,35,23,45,64,84,92]
print(list1[0])
# 34 


# 2. It can store elements of different types (integer,float, string,etc.).
# It means we can store multiple  data types of value in a single List.
student=['karan',34 ,48.2 , 'Bangladesh']
print(student)
# ['karan', 34, 48.2, 'Bangladesh']

# 3. List similar to string.But there are a couple of differences.

# 1.string-immutable [ immutable means it can’t change.]
# 2.List-mutable [mutable means it can change.]

# str='Hello'
# str[0]='y'
# print(str)
# see here we can't change the index [0] value. 
# if we try, it's shows like that -"  'str' object does not support item assignment.
# Because string is immutable.

str1=['karan',34 ,48.2 , 'Bangladesh']
print(str1)
# ['karan', 34, 48.2, 'Bangladesh']
str1[0]='Raju'
print(str1)
# ['Raju', 34, 48.2, 'Bangladesh']
# seen we changed the index number 0 value. In the list we can do this.
# Because List is mutable.

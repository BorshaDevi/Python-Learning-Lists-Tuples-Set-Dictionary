# # 1. A built-in data type that stores a set of values.
# list=[]
# print(type(list))
# # Class 'List'
# print (len(list))
# # 5

# # Lists some property similar to string property.
# # In string, we can go with a particular index and find the character, similar thinks we can do in List.
# list1=[34,4,35,23,45,64,84,92]
# print(list1[0])
# # 34 


# # 2. It can store elements of different types (integer,float, string,etc.).
# # It means we can store multiple  data types of value in a single List.
# student=['karan',34 ,48.2 , 'Bangladesh']
# print(student)
# # ['karan', 34, 48.2, 'Bangladesh']

# # 3. List similar to string.But there are a couple of differences.

# # 1.string-immutable [ immutable means it can’t change.]
# # 2.List-mutable [mutable means it can change.]

# # str='Hello'
# # str[0]='y'
# # print(str)
# # see here we can't change the index [0] value. 
# # if we try, it's shows like that -"  'str' object does not support item assignment.
# # Because string is immutable.

# str1=['karan',34 ,48.2 , 'Bangladesh']
# print(str1)
# # ['karan', 34, 48.2, 'Bangladesh']
# str1[0]='Raju'
# print(str1)
# # ['Raju', 34, 48.2, 'Bangladesh']
# # seen we changed the index number 0 value. In the list we can do this.
# # Because List is mutable.

# # List Slicing
# # This is exactly same to same in string slicing.
# list=[3,56, 78, 48, 67,91]
# slicing=list[1:4]
# print(slicing)
# # [56, 78, 48]
# sli2=list[0:]
# print(sli2)
# # [3, 56, 78, 48, 67, 91]
# sli3=list[:len(list)]
# print(sli3)
# # [3, 56, 78, 48, 67, 91]
# sli4=list[-5:-1]
# print(sli4)
# # [56, 78, 48, 67]


# # List method

# # append(): It added value to the end of the list.

# list=[1,2,3,4,5]
# list.append(6)
# print(list)
# # [1, 2, 3, 4, 5, 6]    There is an add element that is called muted .

# # sort():sort means arranging values in the correct order.

# # 1. Ascending.[ascending means low to high / small to big]
# # 2.Descending.[descending means high to low / big to small]
# #  We can sort a list of numbers and a list of strings. 
# # But we can not sort a list of numbers and strings .

# list=[56,3,7,27,19,5]
# # this is Ascending
# list.sort()
# print(list)
# # [3, 5, 7, 19, 27, 56]

# # this is desending
# list.sort(reverse=True)
# print(list)
# # [56, 27, 19, 7, 5, 3]

# letter=['a','d','c','b','e','g','f']
# letter.sort()
# print(letter)
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# product=["banana","litice","apple","mango"]
# product.sort()
# print(product)
# # ['apple', 'banana', 'litice', 'mango'] There is sort a,b,c order.
# product.sort(reverse=True)
# print(product)
# # ['mango', 'litice', 'banana', 'apple']

# # print(list.sort()) can not write like this.it print none. 

# # reverse():   It reverses the order of the list.

# list1=[4,3,2,1,7,6,5]
# list1.reverse()
# print(list1)
# # [5, 6, 7, 1, 2, 3, 4]
# list2=['a','d','c','b','e','g','f']
# list2.reverse()
# print(list2)
# # ['a','d','c','b','e','g','f']

# # insert():    In this function , we can add the value in the middle of the list.

# # It’s same as the append function. But in the append function,we added value at the end of the list. 
# # Str: val.insert(index,element)
# # First declare which  index add and then in the index what is added. 
# list=[4,3,2,1,7,6,5]
# list.insert(1,8)
# print(list)
# # [4, 8, 3, 2, 1, 7, 6, 5]


# remove(): In this function,we can delete specific value of the list.
# This method will remove the first occurrence of the given value.

list2=[4,5,6,4,9,7,9]
list2.remove(4)
print(list2)
# [5, 6, 4, 9, 7, 9]


# pop(): 
# The  function,It  deletes a  specific index value of the list.
# If no index is provided, it removes and returns the last item of the list by default.
# syntax: val.pop(index)

list3=[1,2,3,4,5,6]
list3.pop()
print(list3)
# [1, 2, 3, 4, 5]
list3.pop()
print(list3)
# [1, 2, 3, 4]
list3.pop(2)
print(list3)
# [1, 2, 4]
# print(list3.pop(1))
# 2 it gives index value. it is not remove the value and not return lists.
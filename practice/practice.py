list=[4,3,2,1,7,6,5]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.append(8)
list.sort()
print(list)

computer_product=['Keyboard',"Mouse",'Sound Box',"Camera","Table"]
computer_product.sort()
print(computer_product)

list3=["banana",'apple','banana']
list3.remove('banana')
print(list3)
# ['apple', 'banana']

tuple=(1,2,3,4,5,6,7)
print(tuple[3:5])
# (4, 5)

print(tuple[:len(tuple)])
# (1, 2, 3, 4, 5, 6, 7)

print(tuple[4:])
# (5, 6, 7)

print(tuple[-5:-1])
# (3, 4, 5, 6)


# 1.write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

movieList=[]
mov1=input("mov1: ")
mov2=input("mov2: ")
mov3=input("mov3: ")
movieList.append(mov1)
movieList.append(mov2)
movieList.append(mov3)
print(movieList)
['3 ideat', 'Golmal', 'darucinidip']

movielist=[]
movielist.append(input('mov1'))
movielist.append(input('mov2'))
movielist.append(input('mov3'))
print(movielist)

# 2.write a program to check if a list contains a palindrome of elements.(Hint: use copy() method)

val=[1,2,3,2,1]
copy_=val.copy()
# reverse_=copy_.reverse() this is wrong. it's return none.
copy_.reverse()
print(copy_)
if(copy_ == val):
    print('palindrome')
else:
    print('not palindrome')    

val1=[1,'abc','abc',1,2]
copy1_=val1.copy()
copy1_.reverse()
print(copy1_)
if(copy1_ == val1):
    print('palindrome')
else:
    print('not palindrome')    


# 3.Write a program to count the number of students with the 'A' grade in the follow tuple.
grade=("C",'D','A','A','B','B','A')
print(grade.count('A'))
# 3

# 4.Store the above values in a list & sort them from 'A' to "D".
list=["C",'D','A','A','B','B','A']
list.sort()
print(list)
# ['A', 'A', 'A', 'B', 'B', 'C', 'D']

# dictionary
dic={}
print(type(dic))
dic.update({'name':'Alvi',"age":16})
print(dic)
getname=dic.get('name')
print(getname)
print(dic.items())
print(list(dic.items()))
print(len(dic))
item=list(dic.items())
print(item[0])
dic1={
    "name":'Alex',
    "age":20,
    "subjects":['phy','math','Bangla','chem','English','history','Bio','zoo','geo'],
    "total years":{
        'first year':{
        'result':3.00,
        'department sub':('math','Bangla','phy'),
    },
    'second year':{
        'result':3.25,
        'department sub':('chem','English','history'),
    },
    'third year':{
        'result':3.50,
        'department sub':('Bio','zoo','geo'),
    },
    }
}
print(dic1.get('total years').get('first year').get('department sub'))
print (dic1["name"])
print(dic1.keys())
print(dic1.values())

# set
pro1=set()
pro1.add(1)
pro1.add(5)
pro1.add('Apple')
pro1.add('orange')
pro1.add('6')
pro1.add('6')
print(pro1)
# {'6', 1, 5, 'Apple', 'orange'}

pro1.remove('Apple')
print(pro1)
# {'6', 1, 5, 'orange'}

print(pro1.pop())
print(pro1.pop())
print(pro1)
pro1.pop()
print(pro1)
pro1.clear()
print(pro1)

# a={1,2,3,3,4}
# b={3,4,5,6,7}
# print(a.union(b))

# print(a.intersection(b))

# 5. Store following word meaning in a python dictionary:
# table:"a piece of furniture","list of facts & figures"
# cat: "a small animal"
dic1={}
newDic1={"table":["a piece of furniture","list of facts & figures"] ,"cat":"a small animal"}
dic1.update(newDic1)
print(dic1)


# 6. You are given a list of subjects for students. Assume one classroom is required for 1 subject.How many classrooms are needed by all students?
sub=['python','java','c++','python','javascript','java','python','java',"c++",'c']
sub1=set(sub)
print(sub1)
print(len(sub1))


# 7. Write a program to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one.Use subject name as key and marks as value.
dic1={}
sub1=int(input('math  :'))
sub2=int(input("Bangla :"))
sub3=int(input('English :'))
dic1.update({'math':sub1})
dic1.update({'Bangla':sub2})
dic1.update({'English':sub3})
print(dic1)



# 8. Figure out a way to store 9 and 9.0 as separate values in the set.(You can take help to built-in data types)
value={9,"9.0"}
val1={
    ("int",9),
    ("float",9.0)
}
print(value)
print(val1)


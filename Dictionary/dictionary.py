# Dictionaries are used to store data values in key:value pairs.
# A dictionary is created by using curly braces.
# They are unordered,mutable(changeable) & don’t allow duplicate keys.
# In a dictionary, values can be of any data type, but keys must be immutable data types, 
# so tuples can be used as keys, whereas lists cannot.

dict={
    "name":'Max',
     "age":54,
     "subjects":['Python','Javascript','C'],
     "topics":('List','tuple','set','dict'),
     'is_adult':True,
     ('morning','eveing','night'):"value"
}
print(dict)

# Syntax: dict[key name]
student={
    "name":'David',
    "age":18,
    "class":12,
    "subject":['Bangla',"English","Math"]
}
print(student['subject'])
# ['Bangla', 'English', 'Math']

# If we need to change any value in a dictionary,it is possible. 
student={
    "name":'David',
    "age":18,
    "class":12,
    "subject":['Bangla',"English","Math",""]
}
student['name']='max'
print(student)
# {'name': 'max', 'age': 18, 'class': 12, 'subject': ['Bangla', 'English', 'Math']}
# see first "name" value is David and now Max

# We can add a new key value pair.
stu={
    "name":'Max',
    "age":17,
    
}
stu["class"]=11
print(stu)
# {'name': 'Max', 'age': 17, 'class': 11}

stu={
    "name":'Max',
    "age":17,
    "name":'David'
}
print(stu)
# {'name': 'David', 'age': 17}

# We can create null dictionary.
null_dict={}
null_dict['name']='David Lucy'
null_dict['age']=16
print(type(null_dict))
# dict
print(null_dict)
# {'name': 'David Lucy', 'age': 16}

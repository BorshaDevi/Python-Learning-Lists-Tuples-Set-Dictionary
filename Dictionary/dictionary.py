# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is created by using curly braces.
# # They are unordered,mutable(changeable) & don’t allow duplicate keys.
# # In a dictionary, values can be of any data type, but keys must be immutable data types, 
# # so tuples can be used as keys, whereas lists cannot.

# dict={
#     "name":'Max',
#      "age":54,
#      "subjects":['Python','Javascript','C'],
#      "topics":('List','tuple','set','dict'),
#      'is_adult':True,
#      ('morning','eveing','night'):"value"
# }
# print(dict)

# # Syntax: dict[key name]
# student={
#     "name":'David',
#     "age":18,
#     "class":12,
#     "subject":['Bangla',"English","Math"]
# }
# print(student['subject'])
# # ['Bangla', 'English', 'Math']

# # If we need to change any value in a dictionary,it is possible. 
# student={
#     "name":'David',
#     "age":18,
#     "class":12,
#     "subject":['Bangla',"English","Math",""]
# }
# student['name']='max'
# print(student)
# # {'name': 'max', 'age': 18, 'class': 12, 'subject': ['Bangla', 'English', 'Math']}
# # see first "name" value is David and now Max

# # We can add a new key value pair.
# stu={
#     "name":'Max',
#     "age":17,
    
# }
# stu["class"]=11
# print(stu)
# # {'name': 'Max', 'age': 17, 'class': 11}

# stu={
#     "name":'Max',
#     "age":17,
#     "name":'David'
# }
# print(stu)
# # {'name': 'David', 'age': 17}

# # We can create null dictionary.
# null_dict={}
# null_dict['name']='David Lucy'
# null_dict['age']=16
# print(type(null_dict))
# # dict
# print(null_dict)
# # {'name': 'David Lucy', 'age': 16}


# # Nested dictionary:
# student={
#     "name":'Raju Kumar',
#     "subjects":{
#         "physics":43,
#         'math':90,
#         'Bangla':80,
#     },
#     "result":{
#            "first year":{
#                "pass":True,
#                'marks':3.00,
#                "subjects":['chem','english','history'],
#            },
#            "second year":{
#                "pass":True,
#                'marks':3.25,
#                "subjects":['phy','english','geo'],
#            },
#            "third year":{
#                "pass":True,
#                'marks':3.50,
#                "subjects":['math','bangla','social science'],
#            },
#     },
# }
# # print(student)
# print(student['name'])
# # Raju Kumar
# print(student['subjects']['math'])
# # 90
# print(student['result']['third year']['subjects'])
# # ['math', 'bangla', 'social science']
# print(student['result']['first year']['subjects'][1])
# # english


# # Method:


# # keys():Returns all keys.
# student={
#     "name":'Lucy',
#     "subjects":{
#         "phy":45,
#         "math":90,
#          'bangla':80,
#     }
# }
# print(student.keys())
# # dict_keys(['name', 'subjects'])

# #  If we need to list the type of these dictionary keys then we do this.
# print(list(student.keys()))
# # ['name', 'subjects']

# #  If we need to know the dictionary length.
# print(len(student))
# # 2
# # or
# print(len(list(student.keys())))
# # 2
# print(list(student['subjects'].keys()))
# # ['phy', 'math', 'bangla']



# # values():Returns all values.
# student={
#     "name":'Lucy',
#     "subjects":{
#         "phy":45,
#         "math":90,
#          'bangla':80,
#     }
# }
# print(student.values())
# # dict_values(['Lucy', {'phy': 45, 'math': 90, 'bangla': 80}])

# print(list(student.values()))
# # ['Lucy', {'phy': 45, 'math': 90, 'bangla': 80}]

# print(len(student.values()))
# # 2

# # If we need to dictionary to dictionaries nested values.Then we do this.
# print(list(student['subjects'].values()))
# # [45, 90, 80]


# # items(): Returns all (key,value) pairs as tuples.
# student={
#     "name":'Lucy',
#     "subjects":{
#         "phy":45,
#         "math":90,
#          'bangla':80,
#     }
# }
# print(student.items())
# # dict_items([('name', 'Lucy'), ('subjects', {'phy': 45, 'math': 90, 'bangla': 80})])
# print(list(student.items()))
# # [('name', 'Lucy'), ('subjects', {'phy': 45, 'math': 90, 'bangla': 80})]

# pairs=list(student.items())
# print(pairs[0])
# # ('name', 'Lucy')

# get(“ key ”):Returns the key according to value.
student={
    "name":'Lucy',
    "subjects":{
        "phy":45,
        "math":90,
         'bangla':80,
    }
}
print(student.get('name'))
# Lucy
# print(student.get('name1'))
# print(student["name1"])


#  what is the different between print(student.get('name1')) and print(student["name1"])
# If print(student.get('name1')) this can not find any value of this key ,it return none.But this can not stop the function.
# But If print(student["name1"]) this can not find any value of this key,it return error.For this error stop the function.
# That's why print(student.get('name')) this use.




# update(newDict):Inserts the specified items to the dictionary.
student={
    "name":'Lucy',
    "subjects":{
        "phy":45,
        "math":90,
         'bangla':80,
    }
}
student.update({'city':'Utora'})
print(student)
# {'name': 'Lucy', 'subjects': {'phy': 45, 'math': 90, 'bangla': 80}, 'city': 'Utora'}
# we can also added like new dictionary in the dictionary.
newDict={"age":15, "class":'9'}
student.update(newDict)
print(student)
# {'name': 'Lucy', 'subjects': {'phy': 45, 'math': 90, 'bangla': 80}, 'city': 'Utora', 'age': 15, 'class': '9'}

# print(student.update({'city':'Utora'})) We can not write  this.

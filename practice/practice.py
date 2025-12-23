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

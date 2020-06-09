#assigning elements to a different list

print("List:")
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
print 'list1 = ', list1
print 'list2 = ', list2
list2=list1
print 'After assigning new list: '
print 'list1 = ', list1
print 'list2 = ', list2

#accessing element in a tuple

print("Tuple:")
tuple=('Hello','hi','bye')
print(tuple[:3])
print(tuple[2])

#deleting an element in a dictionary

print("Dictionary:")
dict={1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
for i in dict.keys():
    if i == 5:
        del dict[i]
print(dict)

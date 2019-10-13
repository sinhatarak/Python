list1=["Hadoop","Python","Linux"]
#list1[0]="Spark"

#print(list1[0:2])

#del(list1[2])

# pop remove the items but will give output
#list1.pop(1)

# list comprehensive func
#list2=[x**2 for x in [1,2,3,4,5]]
#print(list2)


list=[1,2,3]
#list.append("Market") ## Adds an item to the end of the list
#list.extend({'g','j'}) ## Insert many items at the end of list
#list.insert(1,"Scripting") ## Insert the item at given position
#list.remove(1) ## remove an item from the list

#print(sorted(list)) ## sorted out the list
#OR using loop

for x in list[::-1]:
    print(x)


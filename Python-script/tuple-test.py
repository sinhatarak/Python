"""
Tuple is a sequence of immuatable Python objects, Tuples are
just like lists,
It's faster than lists
Tuple has less execution time

example:- tuple=("Market","sales")
"""
#tup1=("Hadoop","Solr","jenkins","Apache")
#var1 = tup1[0]
#print(tup1[0])
#print(len(tup1))
#print(max(tup1))
#print(min(tup1))

#output
"""4
jenkins
Apache
"""
tup2=([0,1],[1,2,4])
tup2[0][0]="updated"
print(tup2)
# Convert tuple into list
lst=list(tup2)
print(lst)

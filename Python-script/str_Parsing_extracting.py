#parsing & Extracting

name = "From taraksinha09@gmail.com Sat Jan 19 09:09:18 2019"

fin = name.find('@')
print(fin)
# result 17

a = name.find(' ',fin)
print(a)
#result 27
result = (name[fin+1:a])
print(result)

#Output gmail.com

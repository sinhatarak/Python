name = {'dog': 'sheru', 'cat': 'pssy', 'horse': "bongo"
         }
#print(name)

for dict,x  in name.items():
    print('Key Items:', dict + ', Value:', x  )
#print('\t Here it is dict\n, \t tarak' )
name1 = 'Hello world'
upper=name1.upper()
print(upper)

lower=name1.lower()
print(lower)

user1=input("Enter your name:- ")
#if user1=='Tarak':
#print("Welcome ", user1)

#else:
#    print("Try again")

if user1=='Tarak':
    print("Your name is correct ", user1.upper())
    print("\n Address:- Bangalore,\n Mob:- 8197522750")
elif user1=="":
    print("Correct name only:")
else:
    print('Try again')
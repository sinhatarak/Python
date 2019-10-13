dog = input("Enter how many dogs you have: ")
try:
    if int(dog) >= 4:
        print ("you have more dogs")
    else:
        print("you have less dogs")
except:
    print("Err: USE numbers only")
    

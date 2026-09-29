userdata = {"name" :[] , "age" :[] , "skills" : []}
dastoor = (input("edame ya tamam : "))
if dastoor == "edame" :
        userdata["name"] = input("enter name : ") 
        userdata["age"] = input("enter age : ")
        userdata["skills"] = input("enter skill : ")
        print(userdata)
        
elif dastoor == "tamam" :
        print("goodbye")
else :
        print("unknown action")
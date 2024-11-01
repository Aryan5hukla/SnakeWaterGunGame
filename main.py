import random

# 1 = snake
# -1 = water
# 0 = gun

Computer = random.choice([1,-1,0])
You = input("Enter S : snake , W : water or G : gun = ")
theCh = {
    "S" : 1 ,
    "W" : -1 ,
    "G" : 0 ,
    "s" : 1 ,
    "w" : -1 ,
    "g" : 0
}
theRevCh = {
    1 : "Snake" ,
    -1 : "Water" ,
    0 : "Gun"
}

You = theCh[You]

print(f"You Chose : {theRevCh[You]} \nComputer Chose : {theRevCh[Computer]}")

if(Computer == You) :
    print("It's a Draw !!")
else :
    if (Computer == 1 and You == -1) : 
        print("You Lose")
    elif (Computer == -1 and You == 1) :
        print("You Win")
    elif (Computer == 1 and You == 0) :
        print("You Win")
    elif (Computer == 0 and You == 1) :
        print("You Lose")
    elif (Computer == 0 and You == -1) :
        print("You Win")
    elif (Computer == -1 and You == 0) :
        print("You Lose")
    else :
        print("Something Went Wrong")
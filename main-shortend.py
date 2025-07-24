# Snake , Water , Gun Game.

'''
1 for snake
-1 for water
0 for gun

'''
import random 
computer = random.choice([-1,0,1])
you = input("Enter your choice: ")
youDict = {"s": 1, "w" : -1, "g" : 0}
younum = youDict[you]
reverseDict = {1: "Snake" , -1: "Water" , 0: "Gun"}
print(f" You choose {reverseDict[younum]}\ncomputer choose {reverseDict[computer]}")
if(computer == younum):
        print("Its a draw :-} ")
else:

    '''
    if(computer == -1 and younum == 1):  (computer - you) = -2
     print("You Win :) !")

    elif(computer ==-1 and younum ==0):  (computer - you) = -1
     print("You Loose :( ")

    elif(computer ==1 and younum ==-1):  (computer - you) = 2
        print("You Win :) ! ")

    elif(computer == 1 and younum ==0):  (computer - you) = 1
        print("You Loose :( ")

    elif(computer == 0 and younum ==-1):  (computer - you) = 1
            print("You Win :) ")

    elif(computer == 0 and younum ==1):   (computer - you) = -1
            print("You Loose :( ")

            # The below logic is written on the basis of the value of computer - you

    else:
      print("Something Went Wrong")

      '''
    
    if((computer - younum) ==-1 or(computer - younum) ==2):
          print("You Loose :-( ")
    else:
        print("You Win :-) ")

# Done Game...  :-) 

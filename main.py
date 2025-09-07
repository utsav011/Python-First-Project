import random
computer = random.choice([-1,0,1])
print("\nSelect One (s for Stone, p for paper, si for scissor)")
youstr = input("Enter your choice : ")
youDict = {"s":1, "p":-1, "si":0}
reverseDict = {1:"Stone",-1:"Paper",0:"Scissor"}

you = youDict[youstr]

print(f" \n You choose : {reverseDict[you]}\n computer choose : {reverseDict[computer]} \n")

if (computer == you):
    print("Its Draw")

else:
    if(computer == 1 and you == -1):
      print("You Win")
    elif(computer == 1 and you ==0):
      print("You Lose")
    elif(computer == -1 and you == 1):
      print("You Lose")
    elif(computer == -1 and you ==0):
      print("You Win")
    elif(computer == 0 and you == 1):
      print("You Win")
    elif(computer == 0 and you == -1):
      print("You Lose")
    
    else:
      print("something went wrong")



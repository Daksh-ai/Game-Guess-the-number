GUESS_NO=33
NO_OF_GUESS=10
while(NO_OF_GUESS>1):
    number=int(input("Enter The Number"))
    if number<GUESS_NO:
        print("HINT:Your Number is Low than Guess Number")
        print("Try,Again!")
        NO_OF_GUESS=NO_OF_GUESS-1
        print("YOU HAVE {} OF GUESS REMANING".format(NO_OF_GUESS))
        continue
    elif number==GUESS_NO:
        print("YOU WIN!")
        NO_OF_GUESS=NO_OF_GUESS-1
        NO_OF_GUESS=10-NO_OF_GUESS
        print("YOU ARE COMPLETED IN {} OF GUESS".format(NO_OF_GUESS))
        break
    else:
        print("HINT:Your Number is High Than Guess Number ")
        print("Try,Again!")
        NO_OF_GUESS=NO_OF_GUESS-1
        print("YOU HAVE {} OF GUESS REMANING".format(NO_OF_GUESS))
        continue
print("GAME OVER!")
         
        
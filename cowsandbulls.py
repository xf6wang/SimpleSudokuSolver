def playGame(num):
    #print(num)
    usrNum = str(input("Please enter in a guess: "))

            
    while usrNum <> num:
        cows, bulls = 0, 0
        if len(usrNum) < 4:
            print("Invalid Input try again")
        else:
            for x in range (4):
                for y in range (4):
                    if usrNum[y] == num[x]:
                        if x == y:
                            cows += 1
                        else:
                            bulls += 1
                        break
            print( "cows: {}, bulls: {}".format(cows, bulls))
            
        usrNum = str(input("Please enter in a guess: "))
    print("You guessed the number!")
  
  
if __name__=="__main__":
    print("Welcome to Cows and Bulls")
    secretNum = int(random.random() * 10000)
    while len(str(secretNum)) < 4:
      secretNum = secretNum * 10
    playGame(str(secretNum))
    print (secretNum)
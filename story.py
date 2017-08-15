def story():
  user_name = input('Please enter your name')
  print('YTou wake up and get coffee, you then see a strange man what do you do?Choose wisely')
  #RobinTTD- fixed the issue of not runnig
  user_response = int(input('1.Call emergency department\n2. fight\n3.ignore'))
  if (user_response == 1):
    #1Call emergency department   
    print ('He breaks into your house before you could make the call')
    user_response = int(input('1.you decide to go outside'))
  #2Fight
  elif (user_response == 2):
    #2Fight
    print("you went outside and tried to punch him....you missed")
    user_response = int(input("1.you try again"))
  #3 ignore him
  elif (user_response == 3):
    print ("you ignored him...nice job...")
    user_response = int(input("1.go get some coffee"))

## create outside()
def outside():
  print ("your now outside, what now")
  user_response = int(input("1.try punching him again\n2.threaten to call the police\n3.still ignore him and go to work"))
  if (user_response == 1):
    #try punching again
    print ("you punched him again this time you knocked him out")
    user_response = int(input("1.leave him there"))
  elif (user_response == 2):
    #2 threaten to call the police
    print("you tried to threaten him into calling the police, he laughed")
    user_response = int(input("1.tell him your an officer"))
  elif (user_response == 3): 
    #3.still ignore him
    print("you ignored him and now he stole your tv")
    user_response = int(input("1.Say Hello"))
  
def hospital():
  print ("you took him to the hospital instead of jail, now what?")
  user_response = int(input("1.Now call the police,\n2.drop him off and go home\n3.buy a new television"))
  if (user_response == 1): 
    #Now call the police
    print("There were officers waiting for you")
    user_response = int(input('1.Tell them this was the robber that stole your tv'))
  elif (user_response == 2):
    #drop him off and go home
    print("you left the problem to the officer and hospital...good job")
    user_response = int(input("1.go home after a long day"))
  elif (user_response == 3):
    #buy a new tv
    print("you went to the store and bought a new tv, you forgot your wallet")
    user_response = int("1.Go home and forget about the tv")
    
def house():
  print("You've arrived home")
  user_response = int(input("1.go back to bed\n2grab a cup of coffee and call it a day\n3.come back and realize you have been robbed"))
  if (user_response == 1):
    #go back to bed
    print("You decided to go to bed...")
    user_response = int(input("1.End of story"))
  elif (user_response == 2):
    #grab a cup of coffee and call it a day
    print("You grabbed a cup of coffee and called it a day")
    user_response = int(input("Robber escaped the hospital and now seeks revenge"))
  elif(user_response == 3):
    #Come back and barely realize that you've been robbed
    print("You come home to realize that you've been robbed")
    user_response = int(input("1.end of story"))
def police_station():
  print("The robber is waiting for you to fight")
  user_response = int(input("1.punch him\n2.call for the police to come\n3.forget about him and go home"))
  if(user_response == 1):
    #punch him
    print("you punched him and was knocked out again...nice job!")
    user_response = int(input("1.end of story"))
  elif(user_response == 2):
    #Call for help
    print("You called for help, police came righ away and finally arrested the criminal")
    user_response = int(input("1.End of story"))
  elif (user_response == 3):
    #forget about him and go home
    print("you left him there only to leave him to be bored")
    user_response = int(input("1.End of story"))
    

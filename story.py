def Begin_Experiment(): 
    user_name = input("Name your unfortunate victim \n")
    print('\nYou awake in a dark, moist, and dimmly lit tunnel. You stand up and look around while rubbing the back of your head, when you feel a small nozzle. You grab it and, without any sencond thoughts, tear it out of your head. You examine the piece of machinery when a hologram of a cloacked man appears. \n\n',
    '"Ah, I see you have awakened already. Would you mind helping me run a little experiment,',user_name,'?" \n')
    print('Enter the number that corresponds to your decision \n\n You are cautious about the man due to the ominous tone in his voice, but you carfully look over your options before continuing\n\n NOTICE: currently void')
    user_response = int(input('1. Agree to help the man. \n2. Throw the holoprojector. \n3. Refuse to help him \n'))
    beginings(user_response, user_name)

def beginings(user_response, user_name):
    if (user_response == 1):
        print('\n "Great,not the best of ideas, but a good one none the less. So now that you have agreed to help me, you will be put through a series of tests and ordeals. Look, here comes the first one!" From deep in the tunnel you hear an engine start up and the sounds of multiple drills and saws grinding up against the tunnel walls. \n\n "Good luck!" You start running in the opposite direction of the sounds, but as they grew closer, you look back to see a giant drill the circumference of the tunnel(30 meters) with multiple sawblades protuding from it. \n')
        print('You quickly think over your options and choose to-')
        user_response = int(input('1. Continue sprinting and complete your task\n2. Accept your fate\n3. Throw the holoprojector out of frustration \n'))
        beginings_second(user_response)
    
    elif (user_response == 2):
        print('\n You throw the holoprojector against the wall and start smashing it into the ground. After a while of smashing it, the holoprojector is reduced to a crushed ball of metal and wires. You stand up and look around, decideing to walk to the left. After a few moments you come to a massive drill the circumference of the tunnel(30 meters) that has multiple sawblades protuding from it. At first you started to run away, but when you realized that it was not active, you-\n')
        user_response = int(input('1. Keep running because you are a little shite\n2. Examine the drill\n3. Impale yourself with one of the saws\n'))
        beginings_third(user_response)

    elif (user_response == 3):
        print('"Ah, such a disappointment, I was hoping you would agree with me but I guess not. I am sorry but I have no need for defects, be gone!" The hologram disappeared and you hear a click sound that echos through out the tunnel. From behind the you a lock was undone and you decide to open the door. You were momentarily blinded by the light that poured out of thr door. After a moment, your eyes adapt to the light and you step though the door. In side was a white room with a large pane of glass for the back wall, you take another step forward, but then the door slams shut and locks...')
        user_response = int(input('1. pound on the door and yell for help \n2. Approach the glass pane \n3. freak out\n'))
        beginings_fourth(user_response)
        
    else:
        error(user_response,user_name)
        
def error(user_response,user_name):
    if(user_response != [1,2,3]):
        print("\nNice try jackass, now follow the instructions. \n\n\n\n"'Enter the number that corresponds to your decision \n\n You are cautious about the man due to the ominous tone in his voice, but you carfully look over your options before continuing')
    user_response = int(input('1. Agree to help the man. \n2. Throw the holoprojector. \n3. Refuse to help him \n'))
    beginings(user_response, user_name) 
    
def beginings_second(user_response):
  if (user_response == 1):
    print ('You ran at full speed looking around the walls for anything that you could use to avoid the drill. You can hear the drill getting closer, but that does not faze you even though it is only roughly 20 meters away. You keep running and notice a door that is indented a little off to the side.\n\n You decied to-\n(distance 20m)')
    user_responce = int(input('1.\nKeep running\n 2. run to the door and knock \n3. stop running\n'))
    beginings_fifth(user_response)
    
  elif (user_responce == 2):
    print ('You stopped running and turned to face the drill...')
    user_responce = int(input('1. Run toward the drill\n2. sit down\n3. strip and start dancing'))
    beginings_sixth(user_response)
  
  elif (user_responce == 3):
    print ('You threw the holoprojector which ended up getting grinded to shreds, but then the drill started to  studder and spark. Some(3)of the saws started to go haywire and shot off toward you...\n')
    user_responce = int(input('1. duck\n 2.lean left\n 3. lean right'))
  
def beginings_third(user_response):
  if (user_response == 1):
    print ('You kept running until you ran out of breath. Your stomach started to growl when you realized that you do not know the last time you ate or drank something. Upon that realization you thought about what would possibly happen to you down here-\n')
    user_response = int(input('1. dying to starvation or thrist \n 2. dying from the drill,should it activate\n3. dying from a weak mentality that causes you to instantly have a mental breakdown which in turn causes you to die faster than from starvation or thirst.\n'))
    
  elif (user_response == 2):
    print ('You turned back ans approached the drill. You examined it and noticed that it had seen far better days, it would not be able to go another 100 meters before breaking down, permanently. Additionally, a lot of the saw arms were rusted and could give at any moment. You found a saw that was still in good condition and was simply rusty around the arm that directly attached to the drill-\n')
    user_response = int(input('Take it with you?\n\nYes(1)                             No(2)\n'))
    
  elif (user_response == 3):
    print ('You approach one of the saws and lower it to your chest when the drill activates and satrts driving forward. You having already made up your mind, do not move out of the way. A few moments later the drills grinds and shreads you apart, moments later you die, but then you realize that death is not the end and you are forever to feel the pain of your dying moments.')
    print ('\n\n\n YOU HAVE PERISHED')
  
def beginings_fourth(user_response):
  #1. pound on the door and yell for help \n2. Approach the glass pane \n3. freak out
  if (user_response == 1):
    print ('You pound on the door and yelled until your throat was hoarse and the bones in your hand broke. After a while your voice starts to die down and your strikes become softer. you slid down the door and fall to your knees, crying. After a few minutes of crying you stand up and look around, deciding that instead of crying you should be looking for a way out.\n')
    user_response = int(input('\n1. Examine the lock and the door\n2. Examine the room\n Examine the glass pane window.\n'))
    
  elif (user_response == 2):
    print ('You approach the glass pane at the back of the room and look out of it only to see what look like a factory, or maybe an incinerator? Upon closer inspection you see a series of converyor belts, rails, and what looks to be... Bodies, traveling the coveryor belts. Some of the bodies looked intact while others were a pile of mush in a bucket. They traveled until the came upon an incinerator in which they were dumped. You-\n')
    user_response = int(input('1. back away\n 2. keep watching\n 3. examine a different part of the incineration chamber\n'))
    
  elif (user_response == 3):
    print ('You look around and start to hyperventalate, you crouch down, clutching your head and eventual falling over into the fetal postion. Vison starts to waver and every thing blurs, suddenly a large smile grew across your face and you could sense your eyes constricting. You slowly stand up and start to laugh hysterically while still wearing that smile. You walk over to the glass oane and start to attack it; punching, kicking, headbutting and every other possible way to damage the pane. With no way to tell the time, you can only assume that a long time(one hour, 27 minutes, 56 seconds) had passed. Suddenly the glass pane, which had shown no signs of giving, had started to crack. The cracks grew across the glass, a bolt of lighting, then it shattered. You took a step forward but then fell to your kness, your fingers, toes, wrists and feet had all be broken with the bones sticking out and being trenched in blood. Blood started to trickle from your forhead and your sadistic smile returened to your face. You looked over to your side and saw a large piece glass that seemed like it could be useful-\n')
    user_response = int(input('Take it(1)                         Leave it(2)\n'))
    
def beginings_fifth(user_response): 
  #\nKeep running\n 2. run to the door and knock \n3. stop running\n
  if (user_response == 1):
    print ('You ran past the door and kept running further down the tunnel, you hear the drill get closer, casuing adrenalin to shoot though your body. You countinue running and approach a double door on the left an d an air vent to the right-\n distance = 17m\n')
    user_response = int(input('1. keep runnig\n2. Run to the doors\n3. run to the air vent'))
    
  elif (user_response ==2):
    print ('You ran up to the door and quickly knocked on it.\n\n"Go Away! I Do Not Want To Get Involved With Your Kind!" yelled a man, followed by the voice of a young girl askeding if everything was alright. You look back at the advancenig drill and you-\n\n')
    user_response = int(input('1. Keep knocking\n2. Try to flatten your self to the door\n3. Accept your fate\n'))
    
  elif (user_response == 3):
    print ('You stopped running and turned to face the drill. You had already given up hope, but you-')
    user_response = int(input('1. Stand and face the drill\n2. Sit down\n3. Run towards the drill\n4. Get you shite together and push on!'))
    
def beginnings_sixth_sixth(user_response): 
  #Run toward the drill\n2. sit down\n3. strip and start dancing
  if (user_response == 1):
    print ('You had arleady broken down and did not want to be living anylonger, so you bolted towards the drill and jumped into it. The sickening sound of flesh begin torn apart, bones being grinded and crushed, blood splattering everywhere. Your last thoughts were-\n\n "Finally, freedom and peace..." but then when you feel your flame go out, it was slowly feed those last moments,causing you to endlessly feel the pain of dying.\n\n YOU HAVE PERISHED...')

  elif (user_response == 2):
    print ('You sat down and waited for death to come. The sounds of grinding and sawing grew louder and louder as your fate came. it. The sickening sound of flesh begin torn apart, bones being grinded and crushed, blood splattering everywhere.\n\n YOU HAVE PERISHED')
    
  if BeigBeginBe(user_response ==3):
      print (' you stripped and started to dance while the drill grew closer. But as it sawed through you it stopped midway, leaving you half dead and bleeding out.')
      user_response = int(input('Pray for a miracle(1)                               Await your end(2)'))

import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

user_input = input("Would you like to go left or right? ")
user_input.lower()
if user_input == "left" or user_input == "l":
  print()
  time.sleep(1)
  print("You found a car but don't have the keys. ")
  time.sleep(2)
  user_input = input("Hotwire the car? ")
  user_input.lower()
  if user_input == "yes" or user_input == "y":
    time.sleep(1)
    print("Are you sure? ")
    print()
    user_input = input("Yes or No? ")
    user_input.lower()
    if user_input == "yes" or user_input == ("y"):
      print("......")
      time.sleep(2)
      print("Leave the country.")
      time.sleep(2)
      print("There is nothing here. No time to turn back now.")
      time.sleep(2)
      print("  GAMEOVER  " * 10000)
  else:
    print("You Win!")
    print('''
                                       .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_'.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  &                    ~-~-~-~-~-~-~-~-~-~   /|
 ejm97    )      ~-~-~-~-~-~-~-~  /|~       /_|\
        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
''')
elif user_input == "right" or user_input == "r":
  print("Restart.")
  time.sleep(1)
  #print("Why...")
  time.sleep(1)
  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" * 3)
  time.sleep(1) 
  print("DOŃ!T ŁET THÊM ŠEE")
  time.sleep(3) 
  print("https://tinyurl.com/GAMEOVERRRRRRRR")
else:
  print()
  print("You must think you're realllll clever...")
  print()
  print("There are no easter eggs here. I assure you.")
  time.sleep(5) 
  print("Alright fine. Since you waited...")
  print()
  user_input = input("1 : 2 : 3? ")
  
if user_input == "1":
  print('''
                                       `$/              
           __                        O$               
       _.-"  )                        $'              
    .-"`. .-":        o      ___     ($o              
 .-".-  .'   ;      ,st+.  .' , \    ($               
:_..-+""    :       T   "^T==^;\;;-._ $\              
   """"-,   ;       '    /  `-:-// / )$/              
        :   ;           /   /  :/ / /dP               
        :   :          /   :    )^-:_.l               
        ;    ;        /    ;    `.___, \           .-,
       :     :       :  /  ;.q$$$$$$b   \$$$p,    /  ;
       ;   :  ;      ; :   :$$$$$$$$$b   T$$$$b .'  / 
       ;   ;  :      ;   _.:$$$$$$$$$$    T$$P^"   /l 
       ;.__L_.:   .q$;  :$$$$$$$$$$$$$;_   TP .-" / ; 
       :$$$$$$;.q$$$$$  $$$$$$$$$$$$$$$$b  / /  .' /  
        $$$$$$$$$$$$$;  $$$$$$$$P^" "^Tb$b/   .'  :   
        :$$$$$$$$$$$$;  $$$$P^jp,      `$$_.+'    ;   
        $$$$$$$$$$$$$;  :$$$.d$$;`- _.-d$$ /     :    
        '^T$$$$$P^^"/   :$$$$$$P      d$$;/      ;    
                   :    $$$$$$P"-. .--$$P/      :     
                   ;    $$$$P'( ,    d$$:b     .$     
                   :    :$$P .-dP-'  $^'$$bqqpd$$     
                    `.   "" ' s")  .'  d$$$$$$$$'     
                      \           /;  :$$$$$$$P'      
                    _  "-, ;       '.  T$$$$P'        
                   / "-.'  :    .--.___.`^^'          
                  /      . :  .'                      
                  ),sss.  \  :  bug                   
                 : TP""Tb. ; ;                        
                 ;  Tb  dP   :                        
                 :   TbdP    ;                        
                  \   $P    /                         
                   `-.___.-'
  ''')
elif user_input == "2":
  print('''
            _____________________________________________________________
| |_   _| || | __| / __|| ||  \/  | _ \/ __|/ _ \| \| |/ __|  |
|   | | | _  | _|  \__ \| || |.,| |  _/\__ \ (_) | .` |\__ \  |
|   |_| |_||_|___| |___/|_||_|  |_|_|  |___/\___/|_|\_||___/  |
|   _     __   _   __ ___   __   _      __         __     ___ |
|  /_\   | _) /_\ |__) |   |  \ /_\\ /'(__   |\ ||/ _ |__| |  |
| /___\__|__)/___\|__\_|___|__//___\|__ __)__|_\||\__||__|_|_ |
||         _.-'-``-._          |      \:::::::::'      /     ||
||       ,'::::::''  `.        |      /::::::'         \     ||
||      ::::::'        :       |      \:::::           /     ||
||      |:::'          |       |      /;'`--'`--'`--'`.\     ||
||      ;:::  .  ,     :       |      \_.`--'.  ,'- '._/     ||
||     :-------::-------:      |      /:  o   ::  o   :\     ||
||     `.__o__.;:.__o__.'      |      \:.____.;:.____.'/     ||
||_____(.:::::(:_)_____.)______|______(.:::::(:_)_____.)_____||
||          _     _            |                             ||
||        ,':`._.':`.          |       \`.`.'`.'`.'`'(       ||
||    ..-':::::::'   `--..     |        :::::::::''  :       ||
||   \:::::::::          /     |        |:::::'      |       ||
||   _`.::::::          `._    |        |::::        |       ||
|| .':::_.`--'.  ,'--'._   `,  |       (.----.  ,----.)      ||
||  `.:::  o   ::  o   :  ,'   |       :  o   ::  o   :      ||
||   ,':`.____.;:.____.' `.    |       `.____.;:.____.'      ||
||__`.:(.:::::(:_)_____.)_,'___|_______(.::::(:_)____.)___SSt||
'-------------------------------------------------------------'
  ''')
elif user_input == "3":
  print('''
             __
.-.__      \ .-.  ___  __
|_|  '--.-.-(   \/\;;\_\.-._______.-.
(-)___     \ \ .-\ \;;\(   \       \ \
 Y    '---._\_((Q)) \;;\\ .-\     __(_)
 I           __'-' / .--.((Q))---'    \,
 I     ___.-:    \|  |   \'-'_          \
 A  .-'      \ .-.\   \   \ \ '--.__     '\
 |  |____.----((Q))\   \__|--\_      \     '
    ( )        '-'  \_  :  \-' '--.___\
     Y                \  \  \       \(_)
     I                 \  \  \         \,
     I                  \  \  \          \
     A                   \  \  \          '\
     |              snd   \  \__|           '
                           \_:.  \
                             \ \  \
                              \ \  \
                               \_\_|

                              ,-'_ `-.                              
                              ::".^-. `.                            
                              ||<    >. \                           
                              |: _, _| \ \                          
                              : .'| '|  ;\`.                        
                              _\ .`  '  | \ \                       
                            .' `\ *-'   ;  . \                      
                           '\ `. `.    /\   . \                     
                         _/  `. \  \  :  `.  `.;                    
                       _/ \  \ `-._  /|  `  ._/                     
                      / `. `. `.   /  :    ) \                      
                      `;._.  \  _.'/   \ .' .';                     
                      /     .'`._.* /    .-' (                      
                    .'`._  /    ; .' .-'     ;                      
                    ; `._.:     |(    ._   _.'|                     
                    `._   ;     ; `.-'        |                     
                     |   / .-'./ .'  \ .     /:                     
                     |  +.'  \ `-.   .\ *--*' ;\                    
                     ;.' `. \ `.    /` `.    /  .                   
                    /.L-'\_: L__..-*     \   ".  \                  
                   :/ / .' `' ;   `-.     `.   \  .                 
                   / /_/     /              \   ;  \                
              |  _/ /       /          \     `./    .               
            `   .  ;       /    .'      `-.   ;      \              
           --  /  /  --   ,    /           `"' \      .             
          .   .  '       /   .'                 `.     \            
             /  /    `  /   /                  |  `-.   .           
        --  .  '   \   /                         `.  `-._\          
       .   /  /       : `*.                    :   `.    `-.        
          .  '    `   |    \                    \    `-._   `-._    
     --  /  /   \     :     ;                    \              |   
   .    .  '           ;                          `.  \      :  ;   
       /  /   `       : \    \                      `. `._  /  /    
  --  .  '  \         |  `.   `.                      `-. `'  /\    
     /  .             ;         `-.              \       `-..'  ;   
 `  .  '   `          |__                     |   `.         `-._.  
_  :  /  \     [bug]    ;`-.                  :     `-.           ; 
    `"  `               |   `.                 \       `*-.__.-*"' \
' /  . \                ;_.  :`-._              `._                /
                       /   `  . ; `"*-._                       _.-` 
                     .'"'    _;  `-.__                     _.-`     
                     `-.__.-"         `""---...___...--**"' |       
                                                  `.____..--'
        ''')
from time import sleep
import os
import sys
def DokiDokiGame():
    Player = input("Please enter your name ")
    os.system("cls")
    sleep(1)
    input("""???
'Heeeeeeeeeyyy!!' """)
    os.system("cls")
    input("I see an annoying girl running toward me from the distance, waving her arms in the air like she's tottaly oblivious to any attention she might draw to herself.")
    os.system("cls")
    input("That girl is Sayori, my neighbor and good friend since we were children.")
    os.system("cls")
    input("You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?")
    os.system("cls")
    input("We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up")
    os.system("cls")
    input("But if she's going to chase after me like this, I almost feel better off running away.")
    os.system("cls")
    input("However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me.")
    os.system("cls")
    input("""Sayori
'Haaahhh...haaahhh...'""")
    os.system("cls")
    input("""Sayori
'I overslept again!'""")
    os.system("cls")
    input("""Sayori
'But I caught you this time!'""")
    os.system("cls")
    input(f"""{Player}
"Maybe, but only because I decided to stop and wait for you.'""")
    os.system("cls")
    input("""Sayori
'Eeehhhhh, you say that like you were thinking about ignoring me!'""")
    os.system("cls")
    input(f"""Sayori
'That's mean, {Player}!'""")
    os.system("cls")
    input(f"""{Player}
'Well, if people stare at you for acting weird then I don't want them to think we're a couple or something'""")
    os.system("cls")
    input("""Sayori
'Fine,fine.'""")
    os.system("cls")
    input("""Sayori
'But you did wait for me, after all.'""")
    os.system("cls")
    input("""Sayori
'I guess you don't have it in you to be mean even if you want to~'""")
    os.system("cls")
    input(f"""{Player}
'Whatever you say, Sayori...'""")
    os.system("cls")
    input("""Sayori
'Ehehe~'""")
    os.system("cls")
    input("We cross the street together and make our way to school.")
    os.system("cls")
    input("As we draw near, the streets become increasingly speckled with other students making their daily commute.")
    os.system("cls")
    input(f"""Sayori
'By the way, {Player}'""")
    os.system("cls")
    input("""Sayori
'Have you decided on a club to join yet?'""")
    os.system("cls")
    input(f"""{Player}
'A club?'""")
    os.system("cls")
    input(f"""{Player}
'I told you already, I'm really not interested in joining any clubs.'""")
    os.system("cls")
    input(f"""{Player}
'I haven't been looking, either.'""")
    os.system("cls")
    input("""Sayori
'Eh? That's not true!'""")
    
    
    
    
    
os.system("cls")
input("This game is not suitable for children or thos who are easily distrubed")
sleep(1)
os.system("cls")
input("Individuals suffering from anxiety or depression may not have a safe experience playing this game. For content warnings, visit: http://ddlc.moe/warning.html")
sleep(1)
os.system("cls")
print("By playing Doki Doki Literature Club, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content.")
input("I agree.")
sleep(1)
os.system("cls")
print("Team Salvato")
sleep(1)
os.system("cls")
sleep(1)
print("                            Doki!")
sleep(0.5)
print("                            Doki!")
sleep(0.5)
print("                         Literature Club!")
sleep(0.5)
print("                         ")
sleep(2)
MainMenu_Options = input("""                            New Game
                            Quit
                            """)
match MainMenu_Options:
    case "New Game":
        DokiDokiGame()
    case "Exit":
        sys.exit()


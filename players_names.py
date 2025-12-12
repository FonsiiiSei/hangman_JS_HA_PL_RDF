#Abfrage der Spielernamen
def getPlayersNames():
    player_list = []
    player_number = 1
    while True:
        try:
            ask_player_amount = int(input(" \n    Wie viele Spieler spielen gegen mich: \n (2-5 Spieler möglich, bitte Zahl eintragen) \n"))    
            if ask_player_amount >= 2 and ask_player_amount <= 5:
                for i in range(ask_player_amount):
                    ask_player_name = input(f"Bitte den Namen von Spieler {player_number} eingeben: \n")
                    player_list.append(ask_player_name)
                    player_number +=1
                break
            else:
                print("\033[91m\n!!!! ERROR !!!! \nBitte eine gültige Spieleranzahl eingeben\n!!!! ERROR !!!!\n\033[0m")
        except ValueError:
            print("\033[91m\nBitte eine gültige Zahl eingeben!\033[0m")

    #Ausgabe an Nutzer
    print(f"\nIn eurem Team sind \n {" ".join(player_list)} \n Viel Erfolg!\n")

    return player_list

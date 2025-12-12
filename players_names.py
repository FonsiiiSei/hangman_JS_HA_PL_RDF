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



word = getRandomWord()
def askForTip(word):
        asking_for_tip = int(input("Möchtet ihr einen Hinweis für das gesuchte Wort erhalten:\n1=ja \n2=nein\n"))
        if asking_for_tip == 1:
            with open("random_words.txt", "r", encoding="utf-8") as file:
                content = file.readlines()
        for line in content:
            line = line.strip()
            if ";" in line:
                w, tipp = line.split(";", 1)
                if w == word:
                    print("Tipp:", tipp)
                    return
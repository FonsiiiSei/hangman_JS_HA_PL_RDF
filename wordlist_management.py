import random;
import Mera_draw;

def getRandomWord():
    return_list = [];
    with open("random_words.txt", "r", encoding="utf-8") as file:
        content = file.readlines();
        for element in content:
            return_list.append(element.strip())
 
    return(return_list[random.randint(1, len(content))]);
  

def checkWord(pWord, pWordAsList, pPlayers):
    failCount = 0;
    emptyList = [];
    for element in pWord:
        emptyList.append("_")

    currentGuess = "";
    currentPlayerIndex = 0;
    while True:
        #first check if its won
        if "_" not in emptyList:
            print("Glückwunsch, ihr habt gewonnen!");
            break;
        
        print(" ".join(emptyList));
        currentGuess = input(f"{pPlayers[currentPlayerIndex]}, Bitte gib deinen guess ab: ");
        
        indices = []
        for i, c in enumerate(pWord):
            if c == currentGuess:
                indices.append(i)

        if indices: #value found
                print("Treffer! Du bist nochmal dran.")
                for i in indices:
                    emptyList[i] = currentGuess;
        
        else:
            failCount = failCount + 1;
            if(failCount == 8):
                Mera_draw.draw_hangmann(failCount);
                print("Game Over.")
                print(f"Das Wort wäre gewesen: {pWord}")
                break;
            else:
                print("leider falsch, nächster is dran ");
                print(" ")
                Mera_draw.draw_hangmann(failCount);
                currentPlayerIndex = (currentPlayerIndex + 1) % len(pPlayers)





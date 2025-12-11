import random;
a = 1;
def getRandomWord():

    return_list = [];
    with open("random_words.txt", "r", encoding="utf-8") as file:
        content = file.readlines();
        for element in content:
            return_list.append(element.strip())
 
    return(return_list[random.randint(1, len(content))]);
  

def checkWord(pWord, pWordAsList, pPlayers):
    print(pWord);
    emptyList = [];
    for element in pWord:
        emptyList.append("_")

    currentGuess = "";
    currentPlayerIndex = 0;
    while True:
        print(" ".join(emptyList));
        currentGuess = input(f"{pPlayers[currentPlayerIndex]}, Bitte gib deinen guess ab: ");
        if currentGuess in pWord:
            print("is drinne, du darfst nochmal");
            emptyList[pWord.index(currentGuess)] = currentGuess;
        else:
            print("leider falsch, nächster is dran");
            ##end of list => last player failed, jump to begin
            if(currentPlayerIndex+1 == len(pPlayers)):
                currentPlayerIndex = 0;
            else:
                currentPlayerIndex = currentPlayerIndex + 1;


                


checkWord(getRandomWord(), [], ["Jonas", "Tim", "Erika"])



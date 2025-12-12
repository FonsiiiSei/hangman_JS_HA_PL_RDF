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
        indices = []

        for i, c in enumerate(pWord):
            if c == currentGuess:
                indices.append(i)

        if indices:
            print("Treffer! Du bist nochmal dran.")
            for i in indices:
                emptyList[i] = currentGuess
        else:
            print("leider falsch, nächster is dran");
            currentPlayerIndex = (currentPlayerIndex + 1) % len(pPlayers)



                


checkWord(getRandomWord(), [], ["Jonas", "Tim", "Erika"])



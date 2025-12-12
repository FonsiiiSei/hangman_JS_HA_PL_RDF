import random;
a = 1;
def getRandomWord():

    return_list = [];
    with open("random_words.txt", "r", encoding="utf-8") as file:
        content = file.readlines();
        for element in content:
            return_list.append(element.strip())

    return(return_list[random.randint(1, len(content))]);




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

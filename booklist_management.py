import random;

def getRandomWord():

    return_list = [];
    with open("random_words.txt", "r", encoding="utf-8") as file:
        content = file.readlines();
        for element in content:
            return_list.append(element.strip())

    return(return_list[random.randint(1, len(content))]);

print(getRandomWord());       
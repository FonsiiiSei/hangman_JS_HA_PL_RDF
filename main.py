import players_names
import wordlist_management

players_list = players_names.getPlayersNames();
randomWord = wordlist_management.getRandomWord();

wordlist_management.checkWord(randomWord, [], players_list)

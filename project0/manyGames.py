games = ["mario kart", "uno", "hide and seek", "spoons"]
print("games I like to play: ")
for game in games:
    print(game + " ")
new_game = ''
while(new_game!='q'):
    new_game = input("type a game you like or hit 'q' : ")
    if(new_game!='q'):
        games.append(new_game)
    print("games we like to play: ")
    for game in games:
        print(game + " ")

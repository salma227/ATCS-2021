games = ["mario kart", "uno", "hide and seek", "spoons"]
print("games I like to play: ")
for game in games:
    print(game + " ")
new_game = input("What's a game you like? ")
games.append(new_game)
print("games we like to play: ")
for game in games:
    print(game + " ")
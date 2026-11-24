print("welcome")
introduction=input("what is your name? ")
print(f"Hello, dear {introduction}!\nWelcome to this game, Guess the number and find the key.")




characters = {
    "Hacker": "A person who can unlock doors using technology.",
    "Detective": "A person who can find clues and solve mysteries.",
    "Scientist": "A person who can solve scientific problems."
}

choice = input("Please choose your character (Hacker / Detective / Scientist): ")

while choice not in characters:
    print("wrong, try again")
    choice = input("Please choose your character (Hacker / Detective / Scientist): ")  

print("Your skill :", characters.get(choice))
print("Please choose anything you think you might need for the game: ")
print(["book", "flashlight","map", "knife"])

room_items = ["book", "flashlight","map", "knife"]

basket = []
while True:
        item = input("Add a item or type done: ")
        if item == "done":
             break
        elif item in room_items :
            basket.append(item)
        else:
                    print("This item is not available.")
        


print(basket)
print("let's start the game \n You look ready!!!")


def lets_guess():
    for i in range(4):
        print("What is the chemical formula of table salt ????  ")
    
        guess=input(str("do you know it?"  ))

        if guess == "Nacl":
              return True

        return False
if lets_guess():
      print("Well done! You found the key!")
else:
      print("you lost the game")

print("see you a nother day")
          

 

     




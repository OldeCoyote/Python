def ask_name():
    name = input("What is your name:")
    print(f"Hello {name}")
    contLoop = True
    while contLoop == True:
        userAnswer = input("Is there anyone else there? (y/n) ")
        if userAnswer == "y":
            name = input("What is there name:")
            print(f"Hello {name}")
        elif userAnswer == "n":
            print("Good bye")
            contLoop = False
        else:
            print("Please answer 'y' or 'n'.")

def sumNumbers():
    loop = True
    while loop == True:
        num1 = input("Type a number: ")
        if num1.isdigit():
            num1 = int(num1)
        num2 = input("Type another number: ")
        if num2.isdigit():
            num2 = int(num2)
        if isinstance(num1, int) and isinstance(num2, int):
            print(f"The total is {num1 + num2}")
        else:
            print("I can't sum strings.")
        if input("Add another number? (y/n)") == "n":
            print("Good bye")
            loop = False

def myMusic():
    songs = []
    loop = True
    while loop == True:
        print("Welcome you your music library")
        userAnswer = input("Show songs: 1 | Add song: 2 | Leave: 3")
        if userAnswer == "1":
            print(songs)        
        elif userAnswer == "2":    
            song = input("Name a song: ")
            songs.append(song)
        elif userAnswer == "3":
            print("Good bye")
            loop = False

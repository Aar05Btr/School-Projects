import mysql.connector

global p1scr,p2scr,p1,p2

p1=input("Enter Player Name:").strip().title()
p1scr=0
p2scr=0

def save_score(player_name, score):
    conn = None
    cursor = None
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="GameSphere@123",
            database="game_db",
            use_pure=True
        )
    cursor = conn.cursor()
    query = """
        INSERT INTO scores (player_name, score)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE 
            score = score + VALUES(score)
        """
    cursor.execute(query, (player_name, score))
    conn.commit()
    print(f"✅ Score updated for {player_name}!")

    if cursor:
            cursor.close()
    if conn and conn.is_connected():
            conn.close()


def get_score(player_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GameSphere@1234",
        database="game_db",
        use_pure=True
    )
    cursor = conn.cursor()
    query = "SELECT score FROM scores WHERE player_name = %s"
    cursor.execute(query, (player_name,))
    result = cursor.fetchone()

    if result:
        print(f"{player_name}'s score is {result[0]}")
        return result[0]
    else:
        print(f"No score found for {player_name}")
        return None
        
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()

def show_leaderboard():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GameSphere@123",
        database="game_db",
        use_pure=True
    )
    cursor = conn.cursor()
    query = "SELECT player_name, score FROM scores ORDER BY score DESC"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("\n🎮 Leaderboard:")
        print("-" * 30)
        print(f"{'Player':<15} {'Score':>10}")
        print("-" * 30)
        for player_name, score in results:
            print(f"{player_name:<15} {score:>10}")
    else:
        print("No scores in the leaderboard yet.")

    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()

while True:
        print("\nChoose Which Game To Play:")
        print("Enter 1 to play Number Guessing Game")
        print("Enter 2 to play Flag Guessing Game")
        print("Enter 3 to play Hangman")
        print("Enter 4 to play Rock Paper Scissors")
        print("Enter 5 to play Tic Tac Toe")
        print("Enter 6 to play Black Jack")
        print("Enter Score to check Player Total Score")
        print("Enter Leaderboard to see the leaderboard")
        print("Enter 0 to Exit")
        choice = input("> ").strip().title()

        tpg=["3","5"]

        if choice == "1":
            print('''How to Play:
                  > The computer chooses a secret number between 10 and 50.
                  > Your goal is to guess the correct number.
                  > After each guess, you'll be told whether your guess is too high, too low, or correct.
                  > Keep guessing until you get it right!
                  🧠 Tip: Use the hints to narrow down your guesses!\n''')
            
            import random
            num=random.randint(10,50)
            ctr=0
            while ctr<5:
                print("You have",(5-(ctr)),"more chances")
                guess=int(input("Guess a number in range 10..50: "))
                if guess==num:
                    print("You win!! :)")
                    p1scr+=1
                    break
                else:
                    ctr+=1
                    if guess>num:
                        print("\nNumber is smaller than your guess\n")
                    else:
                        print("\nNumber is greater than your guess\n")
            if not ctr < 5:
                print("You Lose :( \nThe number was",num)
                
        elif choice == "2":
            print('''How to Play:
                  > A flag of a country will appear on the screen.
                  > Type the name of the country you think the flag belongs to.
                  > You'll be told if you're correct or not.
                  > Try to get as many correct as possible!
                  🧠 Tip: Watch for colors, shapes, and symbols that stand out.\n''')

            import turtle
            import random
            import time

            screen=turtle.Screen()
            screen.title('”GUESS THE COUNTRY FROM THE FLAG”')
            screen.bgcolor('white')

            t=turtle.Turtle()
            t.speed(0)
            t.penup()
            def France():
                t.goto(-150,50)
                t.pendown()
                t.begin_fill()
                t.color("blue")
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()
                
                t.penup()
                t.goto(-50,50)
                t.pendown()

                t.begin_fill()
                t.color('white')
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()

                t.penup()
                t.goto(50,50)
                t.pendown()

                t.begin_fill()
                t.color('red')
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()
                t.goto(-150,50)
                t.pendown()
                t.color('black')
                t.setheading(0)
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(200) 
                    t.left(90)
        
            def Japan():
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color('black')
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(200) 
                    t.left(90)
                t.begin_fill()
                t.end_fill()
                t.penup()
                t.goto(0,100)
                t.pendown()
                t.begin_fill()  
                t.color('red')
                t.circle(50)
                t.end_fill()
            
            def Italy():
                t.goto(-150,50)
                t.pendown()
                t.begin_fill()
                t.color("green")
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()
                
                t.penup()
                t.goto(-50,50)
                t.pendown()

                t.begin_fill()
                t.color('white')
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()

                t.penup()
                t.goto(50,50)
                t.pendown()

                t.begin_fill()
                t.color('red')
                t.setheading(0)
                t.forward(100)
                t.setheading(90)
                t.forward(200)
                t.setheading(180)
                t.forward(100)
                t.setheading(270)
                t.forward(200)
                t.end_fill()
                
                t.goto(-150,50)
                t.pendown()
                t.color('black')
                t.setheading(0)
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(200) 
                    t.left(90)
            
            def Russia():
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color('white')
                t.begin_fill()
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(70)   
                    t.left(90)
                t.end_fill()
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color("blue")
                t.begin_fill()
                for i in range(2):
                    t.forward(300)
                    t.right(90)
                    t.forward(70)
                    t.right(90)
                t.end_fill()
                t.penup()
                t.goto(-150, -20)
                t.pendown()
                t.color("red")
                t.begin_fill()
                for i in range(2):
                    t.forward(300)
                    t.right(90)
                    t.forward(70)
                    t.right(90)
                t.end_fill()
                t.position()
                t.penup()
                t.goto(-150,-90)
                t.pendown()
                t.color('black')
                t.setheading(0)
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(200) 
                    t.left(90)
            
            def Germany():
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color('black')
                t.begin_fill()
                for i in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(70)   
                    t.left(90)
                t.end_fill()
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color("red")
                t.begin_fill()
                for j in range(2):
                    t.forward(300)
                    t.right(90)
                    t.forward(70)
                    t.right(90)
                t.end_fill()
                t.penup()
                t.goto(-150, -20)
                t.pendown()
                t.color("gold")
                t.begin_fill()
                for k in range(2):
                    t.forward(300)
                    t.right(90)
                    t.forward(70)
                    t.right(90)
                t.end_fill()
                t.position()
                t.penup()
                t.goto(-150,-90)
                t.pendown()
                t.color('black')
                t.setheading(0)
                for l in range(2):
                    t.forward(300)  
                    t.left(90)
                    t.forward(200) 
                    t.left(90)

            def Sweden():
                t.penup()
                t.goto(-150,50)
                t.pendown()
                t.color("blue")
                t.begin_fill()
                for i in range(2):
                    t.forward(400)
                    t.right(90)
                    t.forward(250)
                    t.right(90)
                t.end_fill()
                t.penup()
                t.goto(-30,50)
                t.pendown()
                t.pensize(0)
                t.color('yellow')
                t.setheading(270)
                t.begin_fill()
                t.forward(250)
                t.right(90)
                t.forward(30)
                t.right(90)
                t.forward(250)
                t.end_fill()
                t.penup()
                t.goto(-150,-55)
                t.setheading(0)
                t.pendown()
                t.color('yellow')
                t.pensize(0)
                t.begin_fill()
                t.forward(400)
                t.right(90)
                t.forward(30)
                t.right(90)
                t.forward(400)
                t.end_fill()
                t.penup()
                t.pensize(2)
                t.goto(-150,-200)
                t.pendown()
                t.color('black')
                t.setheading(0)
                for l in range(2):
                    t.forward(400)  
                    t.left(90)
                    t.forward(250) 
                    t.left(90)
                    
            t.end_fill()

            def Ukraine():
                t.hideturtle()
                t.speed(0)
                t.penup()
                t.goto(0,0)
                width = 400
                height = 200
                t.goto(-width/2, height/2) 
                t.pendown()
                
                t.color("blue")
                t.begin_fill()
                for i in range(2):
                    t.forward(width)
                    t.right(90)
                    t.forward(height/2)  
                    t.right(90)
                t.end_fill()

                t.penup()
                t.goto(-width/2,-height/2)
                t.pendown()

                t.color("yellow")
                t.begin_fill()
                for i in range(2):
                    t.forward(width)
                    t.left(90)
                    t.forward(height/2)  
                    t.left(90)
                t.end_fill()

                t.penup()
                t.goto(-width/2,-height/2)
                t.pencolor('black')
                t.pendown()
                for i in range(2):
                    t.forward(width)
                    t.left(90)
                    t.forward(height)
                    t.left(90)

            flag_functions = {
                "sweden": Sweden,
                "france": France,
                "italy": Italy,
                "japan": Japan,
                "russia": Russia,
                "germany":Germany,
                "ukraine":Ukraine}
            flags = {
                "Sweden": "sweden",
                "France": "france",
                "Italy": "italy",
                "Japan": "japan",
                "Russia": "russia",
                "Germany":"germany",
                "Ukraine":"ukraine"}

            def gameplay():
                global guess,p1scr
                t.clear()
                t.hideturtle()
                flag = random.choice(list(flags.keys()))
                flag_functions[flag.lower()]()
                guess = turtle.textinput("Guess the Flag","Which country flag is this?")
                if guess.lower() == flag.lower():
                    t.clear()
                    t.penup()
                    t.goto(-50,0)
                    t.pencolor('green')
                    t.write("Well done!✅",font=('Times New Roman',30,'normal'))
                    p1scr+=1
                else:
                    t.clear()
                    t.penup()
                    t.goto(-50,0)
                    t.pencolor('red')
                    t.write("Incorrect!",font=('Times New Roman',30,'normal'))
                    time.sleep(3)
                    t.clear()
                    t.pencolor('Blue')
                    t.write('The answer is... ',font=('Times New Roman',30,'normal'))
                    time.sleep(1)
                    t.clear()
                    t.write(flag,font=('Times New Roman',45,'normal'))
            gameplay()
            def choice():
                while True:
                    choice = turtle.textinput("Do you want to play again?", "Yes/No ")
                    if choice.lower() == "yes":
                        gameplay()
                    else:
                        t.clear()
                        t.write('Thank you',font=('Times New Roman',30,'normal'))
                        break
            choice()

        elif choice == "3":
            print('''How to Play:
                  > Guess the hidden word, one letter at a time.
                  > Each wrong guess draws part of the hangman.
                  > If you guess the whole word before the drawing is complete, you win!
                  > Too many wrong guesses, and it's game over.
                  🧠 Tip: Start with common letters like E, A, S, T, R.\n''')
            
            p2=input("Player 2 Enter Your Name:").strip().title()
            HANGMAN_PICS = ['''
              +---+
                  |
                  |
                  |
                 ===''', '''
              +---+
              O   |
                  |
                  |
                 ===''', '''
              +---+
              O   |
              |   |
                  |
                 ===''', '''
              +---+
              O   |
             /|   |
                  |
                 ===''', '''
              +---+
              O   |
             /|\\  |
                  |
                 ===''', '''
              +---+
              O   |
             /|\\  |
             /    |
                 ===''', '''
              +---+
              O   |
             /|\\  |
             / \\  |
                 ===''']

            def get_secret_word():
                word = input("Enter the secret word: ").lower()
                while not word.isalpha():
                    word = input("Only letters allowed. Enter word again: ").lower().strip()
                print("\n" * 49)
                return word


            def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
                print(hangman_pics[len(missed_letters)])
                print("\nMissed letters:", ' '.join(missed_letters))

                display_word = ''
                for letter in secret_word:
                    if letter in correct_letters:
                        display_word += letter + ' '
                    else:
                        display_word += '_ '
                print("\nWord: " + display_word.strip())

            def play_game():
                secret_word = get_secret_word()
                correct_letters = []
                missed_letters = []
                game_over = False
                global p1scr,p2scr

                while not game_over:
                    display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

                    guess = input("\nUser 2: Guess a letter: ").lower()

                    if len(guess) != 1 or not guess.isalpha():
                        print("Please enter a single alphabet letter.")
                        continue

                    if guess in missed_letters or guess in correct_letters:
                        print("You already guessed that letter.")
                        continue

                    if guess in secret_word:
                        correct_letters.append(guess)

                        all_guessed = all(letter in correct_letters for letter in secret_word)
                        if all_guessed:
                            display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                            print("\n🎉 Congratulations! You guessed the word:", secret_word)
                            game_over = True
                            p1scr+=1
                    else:
                        missed_letters.append(guess)

                        if len(missed_letters) == len(HANGMAN_PICS) - 1:
                            display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                            print("\n💀 Game Over! The word was:", secret_word)
                            game_over = True
                            p2scr+=1

                again = input("\nDo you want to play again? (yes/no): ").lower()
                if again.startswith('y'):
                    print("\n" * 3)
                    play_game()

            play_game()

        elif choice == "4":
            print('''How to Play:
                  > Choose Rock, Paper, or Scissors.
                  > The computer will also make a choice.
                  > First to win N rounds (e.g., 3) wins the game!
                     Rules:
                  Rock beats Scissors
                  Scissors beats Paper
                  Paper beats Rock

                  🧠 Tip: Try to predict patterns, but it's mostly luck!\n''')
            
            import random

            player_score = 0
            comp_score = 0

            n=int(input("Enter how many times u want to play the game:"))

            for i in range (n) :
                c1 = input("Rock, paper or scissors[R,P,S]: ").upper()
                c2 = random.choice(['R', 'P', 'S'])
                
                
                if c1 == "R" and c2 == "P":
                    print("Computer chose",c2)
                    print("Computer wins!")
                    comp_score += 1

                if c1 == "R" and c2 == "S":
                    print("Computer chose",c2)
                    print("Player wins!")
                    player_score += 1

                if c1 == "R" and c2 == "R":
                    print("Computer chose",c2)
                    print("Draw.")

                if c1 == "P" and c2 == "S":
                    print("Computer wins!")
                    comp_score += 1

                if c1 == "P" and c2 == "R":
                    print("Computer chose",c2)
                    print("Player wins!")
                    player_score += 1

                if c1 == "P" and c2 == "P":
                    print("Computer chose",c2)
                    print("Draw.")

                if c1 == "S" and c2 == "R":
                    print("Computer chose",c2)
                    print("Computer wins!")
                    comp_score += 1

                if c1 == "S" and c2 == "P":
                    print("Computer chose",c2)
                    print("Player wins!")
                    player_score += 1

                if c1 == "S" and c2 == "S":
                    print("Computer chose",c2)
                    print("Draw.")

            if player_score > comp_score :
                print("Player won the game.")
                p1scr+=1
            elif comp_score > player_score:
                print("Computer won the game.")
            else :
                print("Draw.")

        elif choice == "5":
            print('''How to Play:
                  > Take turns placing X or O on a 3x3 grid.
                  > The first to line up three in a row (horizontally, vertically, or diagonally) wins.
                  > If the grid fills up with no winner, it's a draw.
                  🧠 Tip: Control the center and block your opponent.\n''')
            
            grid = []
            line = []
            for i in range (3):
                for j in range (3):
                    line.append(" ")
                grid.append(line)
                line = []
             
            def print_grid():
                for i in range(3):
                    print("|", end ="")
                    for j in range(3):
                        print (grid[i][j], "|", end ="")
                    print("")
                     
            def player_turn(turn_p1):
                if turn_p1 == True:
                    turn_p1 = False
                    print(f"It's {p2}'s turn")
                else:
                    turn_p1 = True
                    print(f"It's {p1}'s turn")        
                return turn_p1
             
            def write_cell(cell):
                cell -= 1
                i = int(cell / 3)
                j =  cell % 3  
                if turn_p1 == True:
                    grid[i][j] = p1_symbol
                else:
                    grid[i][j] = p2_symbol
                return grid

            def free_cell(cell):
                cell -= 1
                i = int(cell / 3)
                j =  cell % 3
                if grid[i][j] == p1_symbol or grid[i][j] == p2_symbol:
                    print("This cell is not free")
                    return False
                return True
             
            print("Welcome to the Tic-Tac-Toe !")
            print("")
            print_grid()
            print("")
            p2 = input("Please enter name of player 2 : ").strip().title()
            p1_symbol = input("Please enter the symbol of player 1 : ")
            p2_symbol = input("Please enter the symbol of player 2 : ")
            game = True
            full_grid = False
            turn_p1 = False
            winner = ""

            def win_check(grid, p1_symbol, p2_symbol):
                full_grid = True
                p1_symbol_count = 0
                p2_symbol_count = 0  
                for i in range(3):
                    for j in range(3):
                        if grid[i][j] == p1_symbol:
                            p1_symbol_count += 1
                            p2_symbol_count = 0
                            if p1_symbol_count == 3:
                                game = False
                                winner = p1
                                return game, winner
                        if grid[i][j] == p2_symbol:
                            p2_symbol_count += 1
                            p1_symbol_count = 0
                            if p2_symbol_count == 3:
                                game = False
                                winner = p2
                                return game, winner
                        if grid[i][j] == " ":
                            full_grid = False
                             
                    p1_symbol_count = 0
                    p2_symbol_count = 0
                p1_symbol_count = 0
                p2_symbol_count = 0    
                for i in range (3):
                    for j in range (3):
                        for k in range (3):
                            if i + k <= 2:
                                if grid[i + k][j] == p1_symbol:
                                    p1_symbol_count += 1
                                    p2_symbol_count = 0
                                    if p1_symbol_count == 3:
                                        game = False
                                        winner = p1
                                        return game, winner
                                if grid[i + k][j] == p2_symbol:
                                    p2_symbol_count += 1
                                    p1_symbol_count = 0
                                    if p2_symbol_count == 3:
                                        game = False
                                        winner = p2
                                        return game, winner
                        if grid[i][j] == " ":
                            full_grid = False
             
                        p1_symbol_count = 0
                        p2_symbol_count = 0
                p1_symbol_count = 0
                p2_symbol_count = 0    
                for i in range (3):
                    for j in range (3):
                        for k in range (3):
                            if j + k <= 2 and i + k <= 2:
                                if grid[i + k][j + k] == p1_symbol:
                                    p1_symbol_count += 1
                                    p2_symbol_count = 0
                                    if p1_symbol_count == 3:
                                        game = False
                                        winner = p1
                                        return game, winner
                                if grid[i + k][j + k] == p2_symbol:
                                    p2_symbol_count += 1
                                    p1_symbol_count = 0
                                    if p2_symbol_count == 3:
                                        game = False
                                        winner = p2
                                        return game, winner
                        if grid[i][j] == " ":
                            full_grid = False
                         
                        p1_symbol_count = 0
                        p2_symbol_count = 0
                         
                p1_symbol_count = 0
                p2_symbol_count = 0    
                for i in range (3):
                    for j in range (3):
                        for k in range (3):
                            if j - k >= 0 and i + k <= 2:
                                if grid[i + k][j - k] == p1_symbol:
                                    p1_symbol_count += 1
                                    p2_symbol_count = 0
                                    if p1_symbol_count == 3:
                                        game = False
                                        winner = p1
                                        return game, winner
                                if grid[i + k][j - k] == p2_symbol:
                                    p2_symbol_count += 1
                                    p1_symbol_count = 0
                                    if p2_symbol_count == 3:
                                        game = False
                                        winner = p2
                                        return game, winner
                        if grid[i][j] == " ":
                            full_grid = False
                     
                        p1_symbol_count = 0
                        p2_symbol_count = 0              

                if full_grid == True:
                    game = False
                    winner = ""
                    return game, winner
                else:
                    game = True
                    winner = ""
                    return game, winner
             
            while game == True:
                turn_p1 = player_turn(turn_p1)
                free_box = False
                while free_box == False:
                    cell = int(input("Please enter a number for your case (1 to 9 from left to right and from top to bottom) : "))
                    free_box = free_cell(cell)
                grid = write_cell(cell)
                print_grid()
                game, winner = win_check(grid, p1_symbol, p2_symbol)

            if winner == p1:
                print(f"Winner is {p1} !")
                p1scr+=1
            elif winner == p2:
                print(f"Winner is {p2} !")
                p2scr+=1
            else:
                print(f"Grid is full : equality for {p1} and {p2} !")

        elif choice == "6":
            print('''How to Play:
                  > Try to get as close to 21 as possible without going over.
                  > You’re dealt 2 cards and can choose to:
                    - Hit (get another card) or
                    - Stand (end your turn)
                  > Cards are worth the value based on the order.
                  > Beat the dealer’s score without busting (going over 21).
                  🧠 Tip: If you're under 16 and dealer shows a high card, consider hitting.\n''')
            
            import random

            dealer_hand = []
            your_hand = []
            cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
            playerQuit = False
            dealerQuit = False

            def deal(turn):
                a = random.choice(cards)
                turn.append(a)

            def calc(turn):
                total = 0
                ace_count = 0
                for card in turn:
                    if card in ['J', 'Q', 'K']:
                        total += 10
                    elif card == 'A':
                        ace_count += 1
                        total += 11
                    else:
                        total += card
                while total > 21 and ace_count:
                    total -= 10
                    ace_count -= 1
                return total

            for i in range(2):
                deal(your_hand)
                deal(dealer_hand)

            print("Dealer has", dealer_hand[0], "and X")

            while not playerQuit:
                print("\nYou have", your_hand, "which totals to", str(calc(your_hand)))
                if calc(your_hand) > 21:
                    print("You busted!")
                    break
                print("[1] Hit\n[2] Stay")
                decision = input("Enter choice: ")
                if decision == "1":
                    deal(your_hand)
                elif decision == "2":
                    playerQuit = True
                else:
                    print("Invalid input.")

            while not dealerQuit and calc(your_hand) <= 21:
                if calc(dealer_hand) < 17:
                    deal(dealer_hand)
                else:
                    dealerQuit = True

            player_total = calc(your_hand)
            dealer_total = calc(dealer_hand)

            print("\nFinal hands:")
            print("You have", your_hand, "totaling to", player_total)
            print("Dealer has", dealer_hand, "totaling to", dealer_total)

            if player_total > 21:
                print("You busted. Dealer wins!")
            elif dealer_total > 21:
                print("Dealer busted. You win!")
                p1scr+=1
            elif player_total > dealer_total:
                print("You win!")
                p1scr+=1
            elif dealer_total > player_total:
                print("Dealer wins!")
            else:
                print("It's a tie!")

        elif choice == "Score":
            get_score(p1)
                        
        elif choice == "0":
            save_score(p1, p1scr)
            print("Thanks for playing!")
            break
        
        elif choice == "Leaderboard":
            show_leaderboard()
            
        else:
           print("Invalid input. Try again.")

        if choice in tpg:
            save_score(p2, p2scr)
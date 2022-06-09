import tkinter
from tkinter import messagebox
from string import ascii_lowercase
import random
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time
from words import word_list

parent_w = tk.Tk()
parent_w.geometry("580x530")
parent_w.config(bg="black")
L1 = Label(parent_w, text="JETHA KE JAANBAAZ", width=30, bg='#000000', fg='white', font='Serif 15 bold')
L1.grid(row=0, column=2,columnspan=2)
b1 = tk.Button(parent_w,fg="Black" , text="ROCK PAPER SCISSORS", font='Arial 10 bold', command=lambda: rps(), width=35, height=15, bg='#F4BFBF')
b1.grid(row=1, column=2)
# b1.pack()
b2 = tk.Button(parent_w,fg="black" , text="SNAKE GAME", font='Arial 10 bold', command=lambda: snake(), width=35, height=15, bg='#FFD9C0')
b2.grid(row=2, column=2)
# b2.pack()
b3 = tk.Button(parent_w,fg="black" , text="HANGMAN", font='Arial 10 bold', command=lambda: hangman(), width=35, height=15, bg='#FAF0D7')
b3.grid(row=1, column=3)
# b3.pack()
b4 = tk.Button(parent_w,fg="black" , text="TIC TAC TOE", font='Arial 10 bold', command=lambda: rps(),width=35, height=15, bg='#8CC0DE')
b4.grid(row=2, column=3)


direction = 'right'
snake_score = 0
def rps():
    #main window
    root = tk.Toplevel(parent_w)
    root.title("Rock Paper Scissors")
    root.configure(background="#9b59b6")

    #picture definition
    rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
    paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
    scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
    scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

    #insert picture
    user_label = Label(root, image=scissors_img, background="#9b59b6")
    comp_label = Label(root, image=scissors_img_comp, background="#9b59b6")
    comp_label.grid(row=1,column=0)
    user_label.grid(row=1, column=4)

    #indicators
    user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="White", )
    computer_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
    user_indicator.grid(row=0,column=3)
    computer_indicator.grid(row=0, column=1)

    #messages
    msg = Label(root, font=50, bg="#9b59b6", fg="white" )
    msg.grid(row=3, column=2)

    #update message
    def updateMessage(x):
        msg["text"] = x
        if "Win" in msg['text']:
            msg['fg'] = "#10e348"
        elif "loose" in msg['text']:
            msg['fg'] = "red"
        else:
            msg['fg'] = "Yellow"
    #update user score
    def update_user_score():
        score = int(playerScore["text"])
        score += 1
        playerScore["text"] = str(score)

    def update_comp_score():
        score = int(computerScore["text"])
        score += 1
        computerScore["text"] = str(score)


    #scores
    playerScore = Label(root, text=0, font=500, background="#9b59b6", fg="white")
    computerScore = Label(root, text=0, font=500, background="#9b59b6", fg="white")
    computerScore.grid(row=1, column=1)
    playerScore.grid(row=1, column=3)

    #check winner
    def check_winner(player, computer):
        if player == computer:
            updateMessage("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                updateMessage("You Win!")
                update_user_score()
            elif computer == "paper":
                updateMessage("You lose!")
                update_comp_score()
        elif player == "paper":
            if computer == "rock":
                updateMessage("You Win!")
                update_user_score()
            elif computer == "scissors":
                updateMessage("You lose")
                update_comp_score()
        elif player == "scissors":
            if computer == "paper":
                updateMessage("You Win!")
                update_user_score()
            elif computer == "rock":
                updateMessage("You lose")
                update_comp_score()
        else:
            pass

    #update choices

    choices = ["rock", "paper", "scissors"]
    def updateChoice(x):
        comp_choice = random.randint(0,2)


        if choices[comp_choice] == "rock":
            comp_label.configure(image=rock_img_comp)
        elif choices[comp_choice] == "paper":
            comp_label.configure(image=paper_img_comp)
        elif choices[comp_choice] == "scissors":
            comp_label.configure(image=scissors_img_comp)


        if x == "rock":
            user_label.configure(image=rock_img)
        elif x == "paper":
            user_label.configure(image=paper_img)
        elif x == "scissors":
            user_label.configure(image=scissors_img)

        check_winner(x, choices[comp_choice])
    #buttons
    rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="Black", command=lambda: updateChoice("rock"))
    paper = Button(root, width=20, height=2, text="paper", bg="#FAD02E", fg="Black", command=lambda: updateChoice("paper"))
    scissors = Button(root, width=20, height=2, text="scissors", bg="#0ABDE3", fg="Black", command=lambda: updateChoice("scissors"))
    rock.grid(row=2, column=1)
    paper.grid(row=2, column=2)
    scissors.grid(row=2, column=3)


    root.mainloop()


def snake():

    GAME_WIDTH = 1000
    GAME_HEIGHT = 600
    SPEED = 80
    SPACE_SIZE = 25
    BODY_PARTS = 5
    SNAKE_COLOR = "#00FF00" #0000FF
    FOOD_COLOR = "#FF0000" #FFFF00
    BACKGROUND_COLOR = "#000000"
    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []
            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)
    class Food:
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
    def next_turn(snake, food):
        x, y = snake.coordinates[0]
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE
        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snake.squares.insert(0, square)
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global snake_score
            snake_score += 1
            label.config(text="Score:{}".format(snake_score))
            canvas.delete("food")
            food = Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED, next_turn, snake, food)
    def change_direction(new_direction):
        global direction
        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction
    def check_collisions(snake):
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH:
            print("GAME OVER")
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            print("GAME OVER")
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print("GAME OVER")
                return True
        return False
    def game_over():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    window = tkinter.Toplevel(parent_w)
    window.title("Snake game")
    window.resizable(False, False)


    label = Label(window, text="Score:{}".format(snake_score), font=('consolas',40))
    label.pack()
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    window.mainloop()


def hangman():
    window = tk.Toplevel(parent_w)
    window.title("Hangman")

    photos = [PhotoImage(file="image/hang0.png"), PhotoImage(file="image/hang1.png"),
              PhotoImage(file="image/hang2.png"), PhotoImage(file="image/hang3.png"),
              PhotoImage(file="image/hang4.png"), PhotoImage(file="image/hang5.png"),
              PhotoImage(file="image/hang6.png"), PhotoImage(file="image/hang7.png"),
              PhotoImage(file="image/hang8.png"), PhotoImage(file="image/hang9.png"),
              PhotoImage(file="image/hang10.png"), PhotoImage(file="image/hang11.png")]

    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses = 0
        imgLabel.config(image=photos[0])
        the_word = random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(" ".join("_" * len(the_word)))
        print(the_word)

    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses < 11:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get() == the_word_withSpaces:
                        messagebox.showinfo("Hangman", "You guessed it!")
            else:
                numberOfGuesses += 1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses == 11:
                    messagebox.showwarning("Hangman", "Game Over")

    imgLabel = Label(window)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0])

    lblWord = StringVar()
    Label(window, textvariable=lblWord, font="Consolas 24 bold").grid(row=0, column=3, columnspan=6, padx=10)

    n = 0
    for c in ascii_lowercase:
        Button(window, text=c, command=lambda c=c: guess(c), font="Helvetica 18", width=4).grid(row=1 + n // 9,
                                                                                                column=n % 9)
        n += 1

    Button(window, text="New\nGame", command=lambda: newGame(), font="Helvetica 10 bold").grid(row=3, column=8,
                                                                                               sticky="NSWE")

    newGame()
    window.mainloop()




parent_w.mainloop()
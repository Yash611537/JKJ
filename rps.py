import random
from tkinter import *
from PIL import Image, ImageTk

def rps():

    #main window
    root = Tk()
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
                updateMessage("You loose!")
                update_comp_score()
        elif player == "paper":
            if computer == "rock":
                updateMessage("You Win!")
                update_user_score()
            elif computer == "scissors":
                updateMessage("You loose")
                update_comp_score()
        elif player == "scissors":
            if computer == "paper":
                updateMessage("You Win!")
                update_user_score()
            elif computer == "rock":
                updateMessage("You loose")
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


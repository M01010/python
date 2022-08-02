from random import randint


class game_stats:
    def __init__(self) -> None:
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def add_draw(self):
        self.draws += 1


def ask_bot():
    global bot_choice
    bot = randint(1, 3)
    if bot == 1:
        bot_choice = "rock"
    elif bot == 2:
        bot_choice = "paper"
    elif bot == 3:
        bot_choice = "scissors"
    return bot


def ask_user():
    global user_choice
    textinput = input("\nRock, paper, scissors\n").lower()

    if textinput == "rock":
        user_choice = "rock"
        x = 1
    elif textinput == "paper":
        user_choice = "paper"
        x = 2
    elif textinput == "scissors":
        user_choice = "scissors"
        x = 3
    elif textinput == "exit":
        x = 0
    else:
        x = -1
    return x


def print_statement(x: str):
    global wins, losses, draws
    if x == "win":
        print("You picked", user_choice, "And bot picked", bot_choice)
        print("You won!")
        userstats.add_win()
    elif x == "loss":
        print("You picked", user_choice, "And bot picked", bot_choice)
        print("You lost!")
        userstats.add_loss()
    elif x == "draw":
        print("You  both picked", user_choice)
        print("Its a draw")
        userstats.add_draw()
    elif x == "wrong":
        print("Wrong input\nAvailable commands: rock, paper, scissors, exit")
    elif x == "exit":
        print("Exiting..")
    elif x == "end":
        print("wins:", userstats.wins,
              "losses:", userstats.losses,
              "draws:", userstats.draws)


userstats = game_stats()
while True:
    bot = ask_bot()
    user = ask_user()
    if (user == 1 and bot == 2) or \
       (user == 2 and bot == 3) or \
       (user == 3 and bot == 1):
        print_statement("loss")
    elif user == bot:
        print_statement("draw")
    elif (user == 1 and bot == 3) or \
         (user == 2 and bot == 1) or \
         (user == 3 and bot == 2):
        print_statement("win")
    elif user == -1:
        print_statement("wrong")
    elif user == 0:
        print_statement("exit")
        break
print_statement("end")

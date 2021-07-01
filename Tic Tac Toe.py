class TicTacToe:
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def game_won(self):
        if (self.list1[0][0] == '0' and self.list1[0][1] == '0' and self.list1[0][2] == '0') or (
                self.list1[1][0] == '0' and self.list1[1][1] == '0' and self.list1[1][2] == '0') or (
                self.list1[2][0] == '0' and self.list1[2][1] == '0' and self.list1[2][2] == '0') or (
                self.list1[0][0] == '0' and self.list1[1][0] == '0' and self.list1[2][0] == '0') or (
                self.list1[0][1] == '0' and self.list1[1][1] == '0' and self.list1[2][1] == '0') or (
                self.list1[0][2] == '0' and self.list1[1][2] == '0' and self.list1[2][2] == '0') or (
                self.list1[0][0] == '0' and self.list1[1][1] == '0' and self.list1[2][2] == '0') or (
                self.list1[2][0] == '0' and self.list1[1][1] == '0' and self.list1[0][2] == '0'):
            print("PLAYER 1 WINS !")
            exit()
        elif (self.list1[0][0] == 'X' and self.list1[0][1] == 'X' and self.list1[0][2] == 'X') or (
                self.list1[1][0] == 'X' and self.list1[1][1] == 'X' and self.list1[1][2] == 'X') or (
                self.list1[2][0] == 'X' and self.list1[2][1] == 'X' and self.list1[2][2] == 'X') or (
                self.list1[0][0] == 'X' and self.list1[1][0] == 'X' and self.list1[2][0] == 'X') or (
                self.list1[0][1] == 'X' and self.list1[1][1] == 'X' and self.list1[2][1] == 'X') or (
                self.list1[0][2] == 'X' and self.list1[1][2] == 'X' and self.list1[2][2] == 'X') or (
                self.list1[0][0] == 'X' and self.list1[1][1] == 'X' and self.list1[2][2] == 'X') or (
                self.list1[2][0] == 'X' and self.list1[1][1] == 'X' and self.list1[0][2] == 'X'):
            print("PLAYER 2 WINS !")
            exit()

    def computer_player(self):
        for i in range(5):
            print("PLAYER 1 TURN :")
            pos = int(input("Enter the position : "))
            flag = 1
            while flag == 1:
                if pos in self.list1[0]:
                    flag = 0
                elif pos in self.list1[1]:
                    flag = 0
                elif pos in self.list1[2]:
                    flag = 0
                elif pos not in self.list1[0] and pos not in self.list1[1] and pos not in self.list1[2]:
                    print("Position already occupied , Make another choice !")
                    pos = int(input("Enter the position : "))
                    if pos >= 1 and pos <= 9:
                        for l in range(3):
                            if pos in self.list1[l]:
                                for j in range(3):
                                    for k in range(3):
                                        if self.list1[j][k] == pos:
                                            if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                                self.list1[j][k] = '0'
                                                flag = 0

                    else:
                        print("Invalid choice of position, Make another choice!")
                        self.computer_player()

            if pos >= 1 and pos <= 9:
                for l in range(3):
                    if pos in self.list1[l]:
                        for j in range(3):
                            for k in range(3):
                                if self.list1[j][k] == pos:
                                    if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                        self.list1[j][k] = '0'

            else:
                print("Invalid choice of position, Make another choice!")
                self.computer_player()

            for j in range(len(self.list1)):
                print(self.list1[j])
            print()

            if i >= 2:
                self.game_won()

            if i < 4:
                print("PLAYER 2 TURN :")
                # ROW 1
                if self.list1[0][0] == '0' and self.list1[0][1] == '0' and self.list1[0][2] != 'X':
                    print("Position occupied by computer in this turn : 3")
                    self.list1[0][2] = 'X'
                elif self.list1[0][0] == '0' and self.list1[0][2] == '0' and self.list1[0][1] != 'X':
                    print("Position occupied by computer in this turn : 2")
                    self.list1[0][1] = 'X'
                elif self.list1[0][1] == '0' and self.list1[0][2] == '0' and self.list1[0][0] != 'X':
                    print("Position occupied by computer in this turn : 1")
                    self.list1[0][0] = 'X'
                # ROW 2
                elif self.list1[1][0] == '0' and self.list1[1][1] == '0' and self.list1[1][2] != 'X':
                    print("Position occupied by computer in this turn : 6")
                    self.list1[1][2] = 'X'
                elif self.list1[1][0] == '0' and self.list1[1][2] == '0' and self.list1[1][1] != 'X':
                    print("Position occupied by computer in this turn : 5")
                    self.list1[1][1] = 'X'
                elif self.list1[1][1] == '0' and self.list1[1][2] == '0' and self.list1[1][0] != 'X':
                    print("Position occupied by computer in this turn : 4")
                    self.list1[1][0] = 'X'
                # ROW 3
                elif self.list1[2][0] == '0' and self.list1[2][1] == '0' and self.list1[2][2] != 'X':
                    print("Position occupied by computer in this turn : 9")
                    self.list1[2][2] = 'X'
                elif self.list1[2][0] == 0 and self.list1[2][2] == 0 and self.list1[2][1] != 'X':
                    print("Position occupied by computer in this turn : 8")
                    self.list1[2][1] = 'X'
                elif self.list1[2][1] == '0' and self.list1[2][2] == '0' and self.list1[2][0] != 'X':
                    print("Position occupied by computer in this turn : 7")
                    self.list1[2][0] = 'X'
                # COLUMN 1
                elif self.list1[0][0] == '0' and self.list1[1][0] == '0' and self.list1[2][0] != 'X':
                    print("Position occupied by computer in this turn : 7")
                    self.list1[2][0] = 'X'
                elif self.list1[1][0] == '0' and self.list1[2][0] == '0' and self.list1[0][0] != 'X':
                    print("Position occupied by computer in this turn : 1")
                    self.list1[0][0] = 'X'
                elif self.list1[0][0] == '0' and self.list1[2][0] == '0' and self.list1[1][0] != 'X':
                    print("Position occupied by computer in this turn : 5")
                    self.list1[1][0] = 'X'
                # COLUMN 2
                elif self.list1[0][1] == '0' and self.list1[1][1] == '0' and self.list1[2][1] != 'X':
                    print("Position occupied by computer in this turn : 8")
                    self.list1[2][1] = 'X'
                elif self.list1[1][1] == '0' and self.list1[2][1] == '0' and self.list1[0][1] != 'X':
                    print("Position occupied by computer in this turn : 2")
                    self.list1[0][1] = 'X'
                elif self.list1[0][1] == '0' and self.list1[2][1] == '0' and self.list1[1][1] != 'X':
                    print("Position occupied by computer in this turn : 5")
                    self.list1[1][1] = 'X'
                # COLUMN 3
                elif self.list1[0][2] == '0' and self.list1[1][2] == '0' and self.list1[2][2] != 'X':
                    print("Position occupied by computer in this turn : 9")
                    self.list1[2][2] = 'X'
                elif self.list1[1][2] == '0' and self.list1[2][2] == '0' and self.list1[0][2] != 'X':
                    print("Position occupied by computer in this turn : 3")
                    self.list1[0][2] = 'X'
                elif self.list1[0][2] == '0' and self.list1[2][2] == '0' and self.list1[1][2] != 'X':
                    print("Position occupied by computer in this turn : 6")
                    self.list1[1][2] = 'X'
                # MAIN DIAGONAL
                elif self.list1[0][0] == '0' and self.list1[1][1] == '0' and self.list1[2][2] != 'X':
                    print("Position occupied by computer in this turn : 9")
                    self.list1[2][2] = 'X'
                elif self.list1[1][1] == '0' and self.list1[2][2] == '0' and self.list1[0][0] != 'X':
                    print("Position occupied by computer in this turn : 1")
                    self.list1[0][0] = 'X'
                elif self.list1[2][2] == '0' and self.list1[0][0] == '0' and self.list1[1][1] != 'X':
                    print("Position occupied by computer in this turn : 5")
                    self.list1[1][1] = 'X'
                # SECOND DIAGONAL
                elif self.list1[0][2] == '0' and self.list1[1][1] == '0' and self.list1[2][0] != 'X':
                    print("Position occupied by computer in this turn : 7")
                    self.list1[2][0] = 'X'
                elif self.list1[1][1] == '0' and self.list1[2][0] == '0' and self.list1[0][2] != 'X':
                    print("Position occupied by computer in this turn : 3")
                    self.list1[0][2] = 'X'
                elif self.list1[2][0] == '0' and self.list1[0][2] == '0' and self.list1[1][1] != 'X':
                    print("Position occupied by computer in this turn : 5")
                    self.list1[1][1] = 'X'
                    # ROW 1
                else:
                    if self.list1[0][0] == 'X' and self.list1[0][1] == 'X' and self.list1[0][2] != '0':
                        print("Position occupied by computer in this turn : 3")
                        self.list1[0][2] = 'X'
                    elif self.list1[0][0] == 'X' and self.list1[0][2] == 'X' and self.list1[0][1] != '0':
                        print("Position occupied by computer in this turn : 2")
                        self.list1[0][1] = 'X'
                    elif self.list1[0][1] == 'X' and self.list1[0][2] == 'X' and self.list1[0][0] != '0':
                        print("Position occupied by computer in this turn : 1")
                        self.list1[0][0] = 'X'
                    # ROW 2
                    elif self.list1[1][0] == 'X' and self.list1[1][1] == 'X' and self.list1[1][2] != '0':
                        print("Position occupied by computer in this turn : 6")
                        self.list1[1][2] = 'X'
                    elif self.list1[1][0] == 'X' and self.list1[1][2] == 'X' and self.list1[1][1] != '0':
                        print("Position occupied by computer in this turn : 5")
                        self.list1[1][1] = 'X'
                    elif self.list1[1][1] == 'X' and self.list1[1][2] == 'X' and self.list1[1][0] != '0':
                        print("Position occupied by computer in this turn : 4")
                        self.list1[1][0] = 'X'
                    # ROW 3
                    elif self.list1[2][0] == 'X' and self.list1[2][1] == 'X' and self.list1[2][2] != '0':
                        print("Position occupied by computer in this turn : 9")
                        self.list1[2][2] = 'X'
                    elif self.list1[2][0] == 'X' and self.list1[2][2] == 'X' and self.list1[2][1] != '0':
                        print("Position occupied by computer in this turn : 8")
                        self.list1[2][1] = 'X'
                    elif self.list1[2][1] == 'X' and self.list1[2][2] == 'X' and self.list1[2][0] != '0':
                        print("Position occupied by computer in this turn : 7")
                        self.list1[2][0] = 'X'
                    # COLUMN 1
                    elif self.list1[0][0] == 'X' and self.list1[1][0] == 'X' and self.list1[2][0] != '0':
                        print("Position occupied by computer in this turn : 7")
                        self.list1[2][0] = 'X'
                    elif self.list1[1][0] == 'X' and self.list1[2][0] == 'X' and self.list1[0][0] != '0':
                        print("Position occupied by computer in this turn : 1")
                        self.list1[0][0] = 'X'
                    elif self.list1[0][0] == 'X' and self.list1[2][0] == 'X' and self.list1[1][0] != '0':
                        print("Position occupied by computer in this turn : 5")
                        self.list1[1][0] = 'X'
                    # COLUMN 2
                    elif self.list1[0][1] == 'X' and self.list1[1][1] == 'X' and self.list1[2][1] != '0':
                        print("Position occupied by computer in this turn : 8")
                        self.list1[2][1] = 'X'
                    elif self.list1[1][1] == 'X' and self.list1[2][1] == 'X' and self.list1[0][1] != '0':
                        print("Position occupied by computer in this turn : 2")
                        self.list1[0][1] = 'X'
                    elif self.list1[0][1] == 'X' and self.list1[2][1] == 'X' and self.list1[1][1] != '0':
                        print("Position occupied by computer in this turn : 5")
                        self.list1[1][1] = 'X'
                    # COLUMN 3
                    elif self.list1[0][2] == 'X' and self.list1[1][2] == 'X' and self.list1[2][2] != '0':
                        print("Position occupied by computer in this turn : 9")
                        self.list1[2][2] = 'X'
                    elif self.list1[1][2] == 'X' and self.list1[2][2] == 'X' and self.list1[0][2] != '0':
                        print("Position occupied by computer in this turn : 3")
                        self.list1[0][2] = 'X'
                    elif self.list1[0][2] == 'X' and self.list1[2][2] == 'X' and self.list1[1][2] != '0':
                        print("Position occupied by computer in this turn : 6")
                        self.list1[1][2] = 'X'
                    # MAIN DIAGONAL
                    elif self.list1[0][0] == 'X' and self.list1[1][1] == 'X' and self.list1[2][2] != '0':
                        print("Position occupied by computer in this turn : 9")
                        self.list1[2][2] = 'X'
                    elif self.list1[1][1] == 'X' and self.list1[2][2] == 'X' and self.list1[0][0] != '0':
                        print("Position occupied by computer in this turn : 1")
                        self.list1[0][0] = 'X'
                    elif self.list1[2][2] == 'X' and self.list1[0][0] == 'X' and self.list1[1][1] != '0':
                        print("Position occupied by computer in this turn : 5")
                        self.list1[1][1] = 'X'
                    # SECOND DIAGONAL
                    elif self.list1[0][2] == 'X' and self.list1[1][1] == 'X' and self.list1[2][0] != '0':
                        print("Position occupied by computer in this turn : 7")
                        self.list1[2][0] = 'X'
                    elif self.list1[1][1] == 'X' and self.list1[2][0] == 'X' and self.list1[0][2] != '0':
                        print("Position occupied by computer in this turn : 3")
                        self.list1[0][2] = 'X'
                    elif self.list1[2][0] == 'X' and self.list1[0][2] == 'X' and self.list1[1][1] != '0':
                        print("Position occupied by computer in this turn : 5")
                        self.list1[1][1] = 'X'
                    else:
                        flag = 0
                        for j in range(3):
                            if flag == 1:
                                break
                            for k in range(3):
                                if self.list1[j][k] != '0' and self.list1[j][k] != 'X':
                                    self.list1[j][k] = 'X'
                                    if j == 0 and k == 0:
                                        print("Position occupied by computer in this turn : 1")
                                    elif j == 0 and k == 1:
                                        print("Position occupied by computer in this turn : 2")
                                    elif j == 0 and k == 2:
                                        print("Position occupied by computer in this turn : 3")
                                    elif j == 1 and k == 0:
                                        print("Position occupied by computer in this turn : 4")
                                    elif j == 1 and k == 1:
                                        print("Position occupied by computer in this turn : 5")
                                    elif j == 1 and k == 2:
                                        print("Position occupied by computer in this turn : 6")
                                    elif j == 2 and k == 0:
                                        print("Position occupied by computer in this turn : 7")
                                    elif j == 2 and k == 1:
                                        print("Position occupied by computer in this turn : 8")
                                    elif j == 2 and k == 2:
                                        print("Position occupied by computer in this turn : 9")
                                    flag = 1
                                    break

                for j in range(len(self.list1)):
                    print(self.list1[j])
                print()

                if i >= 2:
                    self.game_won()
            if i == 4:
                print("Game Draw")
                exit()

    def human_player(self):
        for i in range(5):
            print("PLAYER 1 TURN :")
            pos = int(input("Enter the position : "))
            flag=1
            while flag == 1:
                if pos in self.list1[0]:
                    flag = 0
                elif pos in self.list1[1]:
                    flag = 0
                elif pos in self.list1[2]:
                    flag = 0
                elif pos not in self.list1[0] and pos not in self.list1[1] and pos not in self.list1[2]:
                    print("Position already occupied , Make another choice !")
                    pos = int(input("Enter the position : "))
                    if pos >= 1 and pos <= 9:
                        for l in range(3):
                            if pos in self.list1[l]:
                                for j in range(3):
                                    for k in range(3):
                                        if self.list1[j][k] == pos:
                                            if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                                self.list1[j][k] = '0'
                                                flag = 0

                    else:
                        print("Invalid choice of position, Make another choice")
                        self.human_player()

            if pos >= 1 and pos <= 9:
                for l in range(3):
                    if pos in self.list1[l]:
                        for j in range(3):
                            for k in range(3):
                                if self.list1[j][k] == pos:
                                    if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                        self.list1[j][k] = '0'

            else:
                print("Invalid choice of position, Make another choice")
                self.human_player()

            for j in range(len(self.list1)):
                print(self.list1[j])
            print()

            if i >= 2:
                self.game_won()

            if i < 4:
                print("PLAYER 2 TURN :")
                pos = int(input("Enter the position : "))
                flag = 1
                while flag == 1:
                    if pos in self.list1[0]:
                        flag = 0
                    elif pos in self.list1[1]:
                        flag = 0
                    elif pos in self.list1[2]:
                        flag = 0
                    elif pos not in self.list1[0] and pos not in self.list1[1] and pos not in self.list1[2]:
                        print("Position already occupied , Make another choice !")
                        pos = int(input("Enter the position : "))
                        if pos >= 1 and pos <= 9:
                            for l in range(3):
                                if pos in self.list1[l]:
                                    for j in range(3):
                                        for k in range(3):
                                            if self.list1[j][k] == pos:
                                                if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                                    self.list1[j][k] = 'X'
                                                    flag = 0

                        else:
                            print("Invalid choice of position, Make another choice")
                            self.human_player()

                if pos >= 1 and pos <= 9:
                    for l in range(3):
                        if pos in self.list1[l]:
                            for j in range(3):
                                for k in range(3):
                                    if self.list1[j][k] == pos:
                                        if self.list1[j][k] != 'X' and self.list1[j][k] != '0':
                                            self.list1[j][k] = 'X'

                else:
                    print("Invalid choice of position, Make another choice")
                    self.human_player()

                for j in range(len(self.list1)):
                    print(self.list1[j])
                print()

                if i >= 2:
                    self.game_won()

            if i == 4:
                print("Game Draw")
                exit()


    def choose_player(self):
        global ch
        # print("ENTER YOUR CHOICE : ")
        print("1--> Play with human ")
        print("2--> Play with computer ")
        print("3--> Quit game ")
        ch = int(input("ENTER YOUR CHOICE : "))

    def start_playing(self):
        self.choose_player()
        if ch == 1:
            self.human_player()
        elif ch == 2:
            self.computer_player()
        elif ch == 3:
            print("Quiting your game")
            exit()
        else:
            print("Invalid player type choice !")
            print("Re-enter your choice : ")
            self.choose_player()

start = TicTacToe()
start.start_playing()
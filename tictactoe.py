import random

class Board():
    """Board object that prints out the tic-tac toe board into the terminal
    using ASCII """


    line =  ".-----."
    row1 =  "|1|2|3|"
    line2 = "|-----|"
    row2 =  "|4|5|6|"
    line2 = "|-----|"
    row3 =  "|7|8|9|"
    line =  ".-----."

    board = [line, row1, line2, row2, line2, row3, line]

    rows = 6

class TicTacToe():
    """Operates the tictactoe game using the Board object"""
    def __init__(self):
        """Initializes the board to be used to play the tictactoe game"""
        self.board = Board()

    def print_board(self):
        """ Appends each row of the board to build the tictactoe game grid"""
        str_board = ""
        for row in self.board.board:
            str_board += row + "\n"
        print(str_board)

    def whoGoesFirst(self):
        """A function that uses a random number to determine who goes first
        versus the computer.

        Returns a print statement and a boolean (True if the user wins.
        False if the user loses)"""
        randNum = random.randint(1, 10)
        userInput = input("Choose a number between 1 to 10: ")

        if int(userInput) > randNum:
            print("Oh no, You get to go first! >:(\nYou are X's")
            return True
        else:
            print("Damn you suck. You get to go last! >:)\n You are O's")
            return False

    def mark_board(self, number, is_user):
        """Marks with X's and O's the tictactoe board based on the number given
        to the function that relates to the board.

        Returns the marked the board
        """
        assert isinstance(number, int)
        assert 1 <= number <= 9
        symbol = "X" if is_user else "O"

        for i, row in enumerate(self.board.board):
            try:
                indNum = row.index(str(number))
                if row[indNum] not in ["X", "O"]:
                    self.board.board[i] = row[:indNum] + symbol + row[indNum + 1:]
                else:
                    print("Sorry, this spot is already marked. Pick a different square")
                    return self.board.board
            except ValueError:
                continue

        return self.board.board

    def check_winner(self, board):
        """Checks the board if there are the rows or columns in the board are
        the same symbol or if the diagonals going both ways are the same symbol
        """
        winner = ""
        """Checks the rows for any row of 3 X's or O's"""
        for i in range(1, 6, 2):  # Iterate over rows (1, 3, 5)
            if board[i][1] == board[i][3] == board[i][5]:
                return f"{board[i][1]}'s"
        """Checks the columns for any set of 3 X's or O's"""
        for i in range(1, 6, 2):  # Iterate over columns (1, 3, 5)
            if board[1][i] == board[3][i] == board[5][i]:
                return f"{board[1][i]}'s"
        """Checks for any Diagonal set of 3 X's or O's"""
        if board[1][1] == board[3][3] == board[5][5]:
            return f"{board[1][1]}'s"
        if board[1][5] == board[3][3] == board[5][1]:
            return f"{board[1][5]}'s"
        return ""

    def is_empty(self, number):
        return str(number) in ''.join(self.board.board)

    def play_tictactoe(self):
        result = ""
        self.print_board()
        firstPlayer = self.whoGoesFirst()
        count = 0
        while True:
            try:
                if firstPlayer:
                    gridNum = int(input("Choose a number to place your mark: "))
                    assert 1 <= gridNum <= 9
                    if self.is_empty(gridNum):
                        self.mark_board(gridNum, True)
                    else:
                        print("Sorry this spot is already filled")
                        continue
                else:
                    computerMove = random.randint(1, 9)
                    if self.is_empty(computerMove):
                        self.mark_board(computerMove, False)
                    else:
                        print("Sorry this spot is already filled")
                        continue

                self.print_board()

                result = self.check_winner(self.board.board)
                if "X's" in result or "O's" in result:
                    print("WINNER!")
                    break
                else:
                    for i in self.board.board:
                        for char in i:
                            if not char.isdigit() and char not in [".", "-", "|"]:
                                count += 1
                    if count == 36:
                        print("No One Won")
                        break
                firstPlayer = not firstPlayer

            except ValueError:
                print("Sorry this is not a usable character. Choose a number between 1 and 9.")

if __name__ == '__main__':
    print("Welcome to TicTacToe\nI hope you're ready to lose! >:)")
    game = TicTacToe()
    game.play_tictactoe()

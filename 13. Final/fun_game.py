#!/usr/bin/env python3
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   Lab: Topic 13 - Connect Four
# Date:         12 07 2022

"""
A Connect Four Game.
"""

import sys
from pprint import pformat
from tkinter import TclError
import numpy as np
from turtlegame import TurtleGame


class ConnectFour(TurtleGame):
    def __init__(
        self,
        width: int = 900,
        height: int = 900,
        background_color: str = "grey",
        grid_color: str = "black",
        player1_color: str = "red",
        player2_color: str = "yellow",
        title: str = "Connect Four",
    ) -> None:
        super().__init__(width, height, background_color, title)
        # make game board grid (7x6)
        self.player1_color = player1_color
        self.player2_color = player2_color
        self.width = width
        self.height = height
        self.rows = 6
        self.cols = 7
        self.grid = [[0 for i in range(self.rows)] for j in range(self.cols)]
        self.player = 1
        self.state = "welcome"
        self.grid_color = grid_color
        self.log_file = open("ConnectFour.log", "w")

    def run(self) -> None:
        """The main game loop."""
        # sometimes when you exit the game it complains
        # and errors, but we can ignore this
        try:
            while True:
                # check every state
                if self.state == "welcome":
                    self.welcome()
                elif self.state == "play":
                    self.play()
                    if self.is_full():
                        self.state = "game over"
                    if self.check() != 0:
                        self.state = "game over"
                elif self.state == "game over":
                    self.game_over()
                self.update()
        except:
            pass

    def check(self):
        """Check if there is a winner."""
        # use numpy to transpose the board
        grid_np = np.array(self.grid)
        columns = grid_np.T
        flipped = np.fliplr(grid_np)

        # use the walrus operator to check if any of the checks are true
        if (x := self.check_straight(grid_np)) != 0:
            return x
        if (x := self.check_straight(columns)) != 0:
            return x
        if (x := self.check_diag(grid_np)) != 0:
            return x
        if (x := self.check_diag(flipped)) != 0:
            return x
        return 0

    def check_straight(self, rows: list) -> int:
        """
        Checks if there are 4 in a row in a row or column
        """
        for column in rows:
            # keep track of the previous
            # to see how many are the same in a row
            prev = column[0]
            count = 0
            for e in column:
                if prev == e and e != 0:
                    count += 1
                else:
                    count = 1
                    prev = e
                if count == 4:
                    return e
        return 0

    def check_diag(self, x: list) -> int:
        """
        Checks the diagonals of the board to see if there are 4 in a row
        """
        # we know all the possible diags so we can just check them
        for i in range(len(x)):
            for j in range(6):
                if i < 4 and j < 3:
                    if (
                        x[i][j] == 1
                        and x[i + 1][j + 1] == 1
                        and x[i + 2][j + 2] == 1
                        and x[i + 3][j + 3] == 1
                    ):
                        return 1
                    if (
                        x[i][j] == 2
                        and x[i + 1][j + 1] == 2
                        and x[i + 2][j + 2] == 2
                        and x[i + 3][j + 3] == 2
                    ):
                        return 2
                elif i < 4 and j >= 3:
                    if (
                        x[i][j] == 1
                        and x[i + 1][j - 1] == 1
                        and x[i + 2][j - 2] == 1
                        and x[i + 3][j - 3] == 1
                    ):
                        return 1
                    if (
                        x[i][j] == 2
                        and x[i + 1][j - 1] == 2
                        and x[i + 2][j - 2] == 2
                        and x[i + 3][j - 3] == 2
                    ):
                        return 2
        return 0

    def welcome(self) -> None:
        """Display the welcome screen."""
        message = """
                                    Welcome To Connect Four

             Players will take turns placing coins into the board.
        The objective of the game is to be the first to form a horizontal,
             vertical, or diagonal line of four of one's own coins.
                                      First to 4 in a row wins!

                                        Player 1: Red
                                        Player 2: Yellow

                        When in the game click anywhere on the
                          column you want to place your coin.
                    You can exit the game at any time by pressing the
                            exit button or Ctrl+C in the terminal.

                            Click anywhere to play and good luck!


                """
        self.draw_text(message, 425, 650, size=20)
        # if there is a click, change the state to play
        if self.get_mouse_click_pos() is not None:
            self.clear()
            self.state = "play"

    def is_full(self) -> bool:
        """Check if the board is full."""
        return all(x != 0 for x in self.grid[0])

    def cord_to_column(self, x: int) -> int:
        """Converts the x cordinate given to a column value"""
        # these values are based on our board being 900x900
        if x < 150:
            return 0
        if 150 < x < 300:
            return 1
        if 300 < x < 450:
            return 2
        if 450 < x < 600:
            return 3
        if 600 < x < 750:
            return 4
        return 5

    def check_spot(self, x: int) -> int:
        """
        Checks each spot to see if any of that column are filled
        and if so puts the peice one above the filled spot
        if not puts it on the bottom.
        """
        for i in range(7):
            if self.grid[i][x] != 0:
                ylocation = i - 1
                break
            ylocation = i
        return ylocation

    def alter(self, x: int, player: int) -> None:
        """
        Takes input of x cord and the player. Then inserts
        the player into the board/grid
        """
        # x and y will be backwards of cords youd think becuase its a list when changing the grid
        x = self.cord_to_column(x)
        y = self.check_spot(x)

        if self.grid[y][x] == 0:
            self.grid[y][x] = player

    def play(self) -> None:
        """Display the game board and update the game state."""
        self.make_grid(7, 6, 900, 900, self.grid_color, 5)
        self.make_circle_grid(7, 6, 900, 900, self.grid_color, 5, False)
        mouse_pos = self.get_mouse_click_pos()
        if mouse_pos is not None:
            x, _ = mouse_pos
            self.alter(x, self.player)
            # switch players
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.log(pformat(self.grid))
        self.draw_coins()

    def log(self, message: str) -> None:
        """Log a message to the console."""
        self.log_file.write(f"{message}\n")

    def draw_coins(self) -> None:
        """Draw the moves on the board."""
        for i in range(7):
            for j in range(6):
                if self.grid[i][j] == 1:
                    color = self.player1_color
                elif self.grid[i][j] == 2:
                    color = self.player2_color
                else:
                    continue
                row_size = self.width / self.rows
                col_size = self.height / self.cols
                radius = min(row_size, col_size) / 2 - 5
                x = row_size * j + row_size / 2
                y = col_size * i + col_size / 2 - radius

                self.draw_circle(x, y, radius, color)

    def game_over(self) -> None:
        """Display the game over screen."""
        message = "Game Over, Click anywhere to play again"
        self.draw_text(message, 425, 300, size=20, color="green")
        # if there is a click, change the state to play
        if self.get_mouse_click_pos() is not None:
            self.clear()
            self.grid = [[0 for i in range(self.rows)] for j in range(self.cols)]
            self.state = "play"

    def quit(self, e: Exception) -> None:
        """Display the quit screen."""
        self.log_file.close()  # close log file
        print("Thanks for playing, goodbye!")
        # exit the program
        sys.exit()


if __name__ == "__main__":
    game = ConnectFour()
    try:
        game.run()
    except (KeyboardInterrupt, SystemExit, TclError) as e:
        game.quit(e)

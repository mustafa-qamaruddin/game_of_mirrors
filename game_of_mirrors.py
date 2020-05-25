'''
This is a skeleton for the Game of mirror exercise. To run the script, open a Terminal / Command Prompt,
navigate to the directory that contains this file and run 'python game_of_mirrors.py'.
'''

import numpy as np

class Game:
    def __init__(self):
        """
        Constructor of the Game class.
        """
        self.difficulty = '' #'easy', 'medium' or 'hard'
        self.player_guess = '' #e.g. 3,0
        self.exit_point = (0,0)
        self.grid = None #A Grid object

    def ask_difficulty(self):
        """
        asks the user for a string (e.g. 'easy'), and updates the difficulty attribute accordingly
        """

    def create_grid(self):
        """
        create the grid attribute using width and height parameters based on difficulty.
        Ex : if the difficulty is set to easy, then self.grid is a 4x4 Grid object with 3 mirrors
        """


    def compute_exit_point(self):
        """
        computes exit point of the laser beam, using the find_exit_point method
        of the LaserBeam object in the grid attribute
        """

    def print_grid(self):
        """
        displays the Grid object with laser beam entry point
        The display should look like :
          1  2  3  4  5
        1       /
        2
        ->         /
        4
        5   /
        """

    def ask_guess(self):
        """
        asks the user for an "x,y" string and
        updates the player_guess attribute accordingly
        """

    def player_guess_to_coords(self):
        """
        uses the string.split(',') method and string slicing on the player_guess
        attribute (e.g. '5, 3') to return a tuple (e.g. (5,3)). No attribute is updated here.
        """

    def print_result(self):
        """
        uses the above player_guess_to_coords function to compare the tuple
        corresponding to the player_guess "x,y" string with the actual exit_point
        computed with find_exit_point
        displays a Victory or Defeat message to the player accordingly.
        """


class Grid:
    def __init__(self, W, H, nb_mirrors):
        '''
        Constructor of the Grid class.
        Giving parameters to the constructor allows you to create a grid
        object this way : G = Grid(5,5,3).
        The Grid is first created empty. Then, at the end of the constructor,
        we call 2 methods to fill the Grid object, based on the W, H, and nb_mirrors parameters,
        and to initialize the LaserBeam object.
        '''
        self.W = W #width of the Grid
        self.H = H #height of the Grid
        self.nb_mirrors = nb_mirrors
        self.laser_beam = None ### A LaserBeam object
        self.state = [] #list of lists; state[3][2] -> content of the cell on 3rd row and 2nd column

        self.random_build()
        self.init_laser_beam()

    def random_build(self):
        """
        Uses all the attributes of the Grid object to fill the state attribute.
        Givesthe mirrors random position and shape (/ or \).
        Tips :
        1)  [(i,j) for i in range(H) for j in range(W)] will give you all the
            possible coordinates in the grid of size WxH.
        2)  Given an integer n, np.random.choice(range(n), size=k) will return a
            list of k distinct integers in the interval [0, n-1]
        3)  Using tip #2, you can create a list of nb_mirrors random indices, and then
            retrieve the corresponding coordinates in the list from tip #1
        """

    def init_laser_beam(self):
        """
        Picks an initial position for the laser beam based on W and H, and
        computes the initial direction accordingly. Then, updates the self.laser_beam
        attribute with a LaserBeam object using the appropriate parameters
        Note : A LaserBeam can only start from one edge of the Grid.
        """

class LaserBeam:
    def __init__(self, initial_x: int, initial_y: int, ini_dir: tuple):
        """
        Constructor of the LaserBeam object
        """
        self.init_pos = None #np.array of shape (2,); defined using initial_x and initial_y
        self.init_direction = None #np.array of shape (2,); defined using ini_dir

    def is_in_grid(self, pos, W, H):
        """
        returns True if the np.array pos (for position) is in bounds for a Grid
        of size WxH, returns False elseway
        """

    def move(self, prev_pos, prev_dir, grid):
        """
        Simulates the movement of the laser beam during one time interval, starting from
        prev_pos (for previous position) and moving in prev_dir (for previous direction).
        Then, computes new direction based on the content of the current visited
        cell in the grid (/, \ or nothing).
        Finally, returns a tuple of size 3 (pos, dir, state) where :
            pos is the new position of the laser beam
            dir is the new direction of the laser beam
            state is the current state of the laser beam ('moving' if it is still in bounds, 'stopping' if not)
        Note : No attribute needs to be altered here.
        """

    def find_exit_point(self, grid):
        """
        Uses the move method until the laser beam stops (out of bounds).
        Then, returns the final position of the laser beam as the exit point,
        using the tuple type.
        """

if __name__ == '__main__':
    """
    The previous condition (__name__=='__main__') is True when this Python script
    is ran as the main script.
    This means that if you want to use the objects from this file in another script,
    without starting the game itself, you can 'import game_of_mirrors' and the
    condition above will be False, so the actions below will not be executed.
    """
    game = Game()
    game.ask_difficulty()
    game.create_grid()
    game.compute_exit_point()
    game.print_grid()
    game.ask_guess()
    game.print_result()

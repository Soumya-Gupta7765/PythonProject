			                             MINESWEEPER 
										 
--main.py
--game_logic.py
--pytxt.txt
--board.py
--file_manager.py



Setup Instructions:

Create a project folder
Create a python file inside the folder, The program automatically creates and uses a saved file pytext
Run the game, open terminal inside the project folder and run 


Game Instructions:

The objective is to uncover all cells without detonating any mines hidden under some squares.
Click a cell to reveal it: if it’s a mine, the game ends; if not, you'll see either a blank or a number.
Numbers show how many mines are adjacent to that cell (including diagonally).
Use flags to mark cells you suspect contain mines.
Use logic and the numbers revealed to deduce safe cells and avoid mines.
Win by revealing all safe cells; lose if you uncover a mine.


Code explanation
First, we are importing random module. 

#Initialising variables
Then we are fixing row and column as 9 because we want a 9X9 grid.
And we are taking number of mines to be 10

#Creating class Cell
Every subdivision in 9 X 9 grid is a cell, which we will define using class cell which will have characteristics mine, revealed, flagged and adjacent. Initializing that every cell at beginning of game is not a mine, not revealed, not flagged and neither adjacent to a mine.

#Creating Board (9X9 Grid)
By using random module, we will randomly generate coordinates for placing the mines. (random.randint) . Then we will set the respective cell’s mine status, whose coordinates were randomly generated to be True. Then we will check all the cells on the 9X9 grid, and if its not a mine we will count the number of adjacent mines. 

#Count adjacent
We will check the surrounding 8 cells adjacent to a particular cell and check whether it contains a mine or not. And if it’s a mine we will add it to a variable count accordingly and return it.


#Reveal cell
If cell is already revealed or flagged, we will return NULL value otherwise we will reveal it. If the cell is not a mine and has zero adjacent mines the function must uncover all its neighbors. To do this it loops through the 8 surrounding directions and recursively the function on each neighboring cells.

#reveal_all_mines and check_win functions
If the player hits any one of the mine reveal_all_mines will reveal all the remaining mines accordingly. Check_win will go through all cells of 9X9 grid, and if  any mine is not revealed and all the cells which do not have mine is revealed then this function will return true.

#Display board
For every row we have to take a list and append the corresponding symbols to it and print for all the rows. This function uses various symbols to give a display on the command line. It represents mine using ‘*’ symbol and normal cell using ‘■’ symbol and flagged cell using ‘⚑ ’ symbol. If the cell doesn’t contain any adjacent mine then we will give space for notation.

#save_game 
The save_game function stores the current situation of the game in a text file. The first line includes board dimension, number of mines and rows, columns. It scans  all the cells for mines and append it to the second line of the file. It scans all the cells which are revealed and append them into the third line of the file. It scans for all the flagged cells and append them in forth line. 


#load_game
The load_game function brings back the previously saved game by reading the file . It reads the file and opens it in “a+” mode. It read all the lines into a list called lines. If the file is empty the function return NULL. It creates board and then reads the second line of the saved file, which contain all mine locations (r, c). Then it reads the third and forth line for revealed cells and flagged cells respectively. It leaves a message “save loaded”. 

#has_save and remove_save
It checks whether a previously saved game exist or not. This function is used whether player starts the game to determine a saved game should be offered for loading. 
Remove_save clears the save file by opening it in write mode and writing an empty string. This is used when a game end either by losing or winning. 

#Play function 
This function contains main game loop and handles user interaction, when the game starts it checks whether a saved files exist or not. If the saved game is found, it will ask the user whether they want to load. If we input an action (r) or (f), it will respectively call the reveal and flag cell function. If the reveal leads to a win, the game also end and save is removed . Flagging simply toggles the flagged state of the chosen cell. The loop continues until the game ends making the play function the centre controller of gameplay.

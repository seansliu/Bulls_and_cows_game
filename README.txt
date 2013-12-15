Shih-Chun Liu sl3497

1. How to use this program.
With 'bullsandcows.py' in the same folder, run 'BullsandCowsGUI.py' in the 
Python Shell. The game window should pop up, and follow the instructions
from there.

2. Design decisions.
I decided to keep three functions (generating a random number, evaluating
bulls and cows, and checking the user's guess) from my original bulls and 
cows game because I thought they would be useful for playing the game.
Then in my GUI I set up six frames, one for the directions, one for the 
player entry, one for the player's record, one for the play button, one
for the quit button, and one to display the average number of tries to win.
For better efficiency, I decided to keep track of the player's guesses and
bulls and cows in one frame that would add a new line after each guess. 
Even though this causes the window to keep getting longer, it allows the
player to keep entering his guess in the same frame.
To keep track of the average number of tries to win, I created variables
inside my class: tries, wineries, and win. Tries increases after every 
try, and wins increases after every win. Whenever the player wins, the 
current tries will be added to wintries, and then tries will reset to 0 for
the new game. The average number of tries to win is the quotient of 
wintries and wins.

3. Conclusions.
Writing classes and widgets is useful for creating objects and data types 
that don't currently exist in the programming language. It's very convenient
to do so for creating visual games like Bulls and Cows.
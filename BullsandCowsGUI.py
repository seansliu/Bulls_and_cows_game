#******************************************************************************
# Shih-Chun Liu
# sl3497
# 4/21/2013
# file: BullsandCowsGUI.py
#
# This program allows a user to play the game Bulls and Cows in a
# Guest User Interface.
#******************************************************************************
import Tkinter as T
import bullsandcows as bc

class BullsCowsGUI:
    def __init__(self):
        '''defines the GUI window'''
        self.main_window = T.Tk()
        self.main_window.title('Bulls and Cows')

        # Create the window frames
        self.top_frame = T.Frame()
        self.mid_frame = T.Frame()
        self.track_frame = T.Frame()
        self.play_frame = T.Frame()
        self.quit_frame = T.Frame()
        self.stats_frame = T.Frame()

        # Directions frame.
        self.message = T.StringVar(value = 'Welcome. Press Play to begin.')
        self.message_label = T.Label(self.top_frame, \
                                     width = 50, bg = 'cyan', \
                                     textvariable = self.message)
        self.message_label.pack(side = 'left')

        # Player input frame.
        self.entry = T.Entry(self.mid_frame, width = 5)
        self.enter_button = T.Button(self.mid_frame, \
                                     text='Guess', command = self.play)
        self.entry.pack(side = 'left')
        self.enter_button.pack(side = 'left')

        # Guess tracking frame.
        self.tracker = T.StringVar()
        self.tracker_label = T.Label(self.track_frame, \
                                     textvariable = self.tracker)
        self.tracker_label.pack(side = 'left')

        # Play and Quit frames.
        self.play_button = T.Button(self.play_frame, \
                                    text = 'Play', \
                                    command = self.start)
        self.quit_button = T.Button(self.quit_frame, \
                                    text = 'Quit', \
                                    command = self.quit_now)
        self.play_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        # Stat tracking frame.
        self.stats = T.StringVar(value = 'Avg. number of guesses to win: ')
        self.stats_label = T.Label(self.stats_frame, \
                                   textvariable = self.stats)
        self.stats_label.pack(side = 'left')

        # Pack frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.track_frame.pack()
        self.play_frame.pack(side = 'left')
        self.quit_frame.pack(side = 'right')
        self.stats_frame.pack()

        # Variables needed in play function.
        self.comp = T.StringVar()
        self.tries = T.IntVar()
        self.wintries = T.IntVar(value = 0)
        self.wins = T.IntVar(value = 0)
        
        T.mainloop()

    def start(self):
        '''resets all the initial values for the game'''
        self.comp.set(bc.random_number(4))
        self.message.set('I have chosen my number. Make your guess.')
        self.tracker.set('')
        self.tries.set(0)

    def play(self):
        '''plays the game bulls and cows'''
        comp = self.comp.get()
        # Check whether computer has a number.
        if comp != '':
            guess = self.entry.get()
            # Check whether player's guess is valid.
            if bc.check_guess(guess, 4):
                # Update bulls and cows and tries for the user.
                self.message.set('I have chosen my number. Make your guess.')
                bulls, cows = bc.bullscows(guess, comp)
                tries = self.tries.get() + 1
                self.tries.set(tries)
                result = 'Guess ' + str(tries) + ': ' + guess + \
                          '  Bulls: ' + bulls + '  Cows: ' + cows
                self.tracker.set(result + '\n' + self.tracker.get())
                
                # Check whether player wins.
                if bulls == '4':
                    self.message.set('Congratulations, you win! ' + \
                                     'Press Play to replay.')
                    self.comp.set('')
                    # Update average tries to win.
                    wins = self.wins.get() + 1
                    self.wins.set(wins)
                    wintries = self.wintries.get() + tries
                    self.wintries.set(wintries)
                    avg = str(float(wintries)/wins)
                    self.stats.set('Avg. number of guesses to win: ' + avg)
                    
                # Max number of tries is 10.
                elif tries == 10:
                    self.message.set('Sorry, you lose! My number was ' + \
                                     comp + '. Press Play to replay.')
                    self.comp.set('')
            else:
                # Invalid guess does not count as a try.
                self.message.set('Invalid guess. ' + \
                                 'Please input only a 4 digit number.')
                
    def quit_now(self):
        '''destroys the GUI'''
        self.main_window.destroy()


bullsandcows = BullsCowsGUI()

from tkinter import Tk, Label, Button


class Game():
    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"
        self.coord = {}
        self.status = 0
        self.counter = 0
        for x in range (3):
            for y in range (3):
                self.coord[y,x] = " "
        self.player1_played = []
        self.player2_played = []

    def status_caller(self):
        self.game_status(self.player1_played,self.player2_played)

    def game_status(self, player1_played, player2_played):
        correct_set = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        print (player1_played, player2_played)

        if (len(self.player1_played) < 3):
            return 2 #not check

        elif (self.counter == 9):
            return -1 #tie

        else:
            for i in correct_set:
                correct_counter = 0

                for j in self.player1_played:
                    if (j in i):
                        correct_counter += 1




#create GUI for the game
class gameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("tic tac toe")
        ##self.master.geometry("350x350")
        self.game = Game()
        self.block_collection = {}
        for x,y in self.game.coord:
            block = Button(self.master, command = lambda x=x,y=y: self.place(x,y), height = 5, width = 10)
            block.grid(row = y, column = x)
            self.block_collection[x,y] = block
        self.reset_button = Button(master, text="reset", command=self.reset, width = 10)
        self.reset_button.grid(row = 4)


    def reset(self):
        self.game = Game()

    def place(self,x,y):
        if self.block_collection[x,y]['state'] != "disabled":
            if self.game.status == 0:
                self.block_collection[x, y]['text'] = self.game.player1
                self.game.status = 1
                self.game.player1_played.append((y*3)+(x+1))
                self.game.counter +=1
            elif self.game.status == 1:
                self.block_collection[x,y]['text'] = self.game.player2
                self.game.status = 0
                self.game.player2_played.append((y*3)+(x+1))
                self.game.counter +=1
            self.block_collection[x,y]['state'] = "disabled"
        self.game.status_caller();
root = Tk()
my_gui = gameUI(root)
root.mainloop()
from tkinter import *
import random



class EggRoulette(Frame):

    def __init__(self, master):

        super(EggRoulette, self).__init__(master)
        self.eggs = ["boiled", "boiled", "boiled", "boiled", "boiled", "raw"]

        self.grid()
        self.create_game()

    def create_game(self):
        imageEgg = PhotoImage(file="egg.ppm")
        w = Label(self, image=imageEgg)
        w.photo = imageEgg
        w.grid(row=2, column=1, columnspan=3)



    def animations(self):

        photo = PhotoImage(self, file="egg2.gif")
        label = Label(self, image=photo)
        label.photo = photo
        label.pack()

    def roulette(self):

        thing = random.choice(self.eggs)
        if thing == "raw":
            self.endGame()
        else:
            self.eggs.remove("boiled")
            return True

    def endGame(self):
        exit()

root = Tk()
root.title("Egg Roulette")
game = EggRoulette(root)
root.mainloop()

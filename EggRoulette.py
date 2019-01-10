from tkinter import *
import random



class EggRoulette(Frame):

    def __init__(self, master):

        super(EggRoulette, self).__init__(master)
        self.eggs = ["boiled", "boiled", "boiled", "boiled", "boiled", "raw"]

        self.grid()
        self.create_game()

    def create_game(self):
        imageEgg = PhotoImage(file="egg.jpg")
        w = Label(self, image=imageEgg)
        w.photo = imageEgg
        w.grid(row=2, column=1, columnspan=3)

        self.bttn1 = Button(self, text="Press for egg")
        self.bttn1["command"] = self.roulette()

        self.bttn1.grid(self, column=0, row=0, )

    def animations(self):
        photo = PhotoImage(file="path/to/image.gif")
        photo.grid()
        #label = Label(image=photo)
        #label.pack()

    def roulette(self):

        thing = random.choice(self.eggs)
        if thing == "raw":
            self.endGame()
        else:
            self.eggs.remove("boiled")
            return True

    def endGame(self):
<<<<<<< HEAD
        # insert GIFs
        return 0
=======
         exit()

>>>>>>> origin/master

root = Tk()
root.title("Egg Roulette")
game = EggRoulette(root)
root.mainloop()
